from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import pandas as pd
from selenium import webbrowser

def getComps():
    url = r'https://regeneration.gr/participating-companies'
    company_name = []

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    section1 = soup.find('section', class_='appearanim builder builder--logogallery')
    div = section1.find('div', class_='wrapper')
    for img in div.find_all('img', alt=True):
        c = "\n".join([img['alt']])
        company_name.append(c)
    return company_name

def get_address():
    search = r'https://www.google.com/webhp?client=firefox-b-d'


df = pd.DataFrame(company_name, columns=["Companies"])
df['City'] = ""
df['Region'] = ""
df['Field'] = ""
df.to_csv('list.csv', index=False)