# Libraries
from selenium import webdriver
import time
import csv


# import PIL


# Functions
def fetch_image_urls(query: str, max_links_to_fetch: int, wd: webdriver, sleep_between_interactions: int = 1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

    # build the google query
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    # load the page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)

        print(
            f"Found: {number_results} search results for {query}. Extracting links from {results_start}:{number_results}")

        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # extract image urls
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)
    url_dict = {f'{query}': image_urls}
    return url_dict


# Needed vars
folder_path = r'C:\Users\Kyriakos\Desktop\ImageStorage'
path = r"C:\Program Files (x86)\chromedriver.exe"
wd = webdriver.Chrome(path)
wd.get("https://google.com")

# Dictionary Write
list = ["sea wallpaper", 'green landscape', 'night city wallpaper']
mega_dict = {}
url_num_fetch = int(input("How many image URL do you want fro this keyword? "))
for i in list:
    url_extract = fetch_image_urls(i, url_num_fetch, wd)
    mega_dict.update(url_extract)
print(mega_dict.values())

# Write to CSV
with open('test.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["KeyWord", "URL"])
    for key, items in mega_dict.items():
        for item in items:
            w.writerow([key, item])

# Need to install webdriver of chrome. check version in settings.
# Link for Webdriver: https://chromedriver.chromium.org/downloads

# The function fetch_image_urls expects three input parameters:
# query : Search term, like Dog(str)
# max_links_to_fetch : Number of links the scraper is supposed to collect(int)
# webdriver : instantiated Webdriver (int)
