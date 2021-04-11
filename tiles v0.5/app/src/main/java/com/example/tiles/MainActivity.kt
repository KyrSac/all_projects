package com.example.tiles

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.graphics.Color
import android.widget.TextView
import android.widget.Toast
import kotlin.math.roundToInt
import kotlin.random.Random
import kotlin.random.nextInt


class MainActivity : AppCompatActivity() {
    //ACTIVE PLAYER
    var activePlayer = 1
    //PLAYER POINTS
    private var p1points:Int = 0
    private var p2points:Int = 0
    private var p3points:Int = 0
    private var p4points:Int = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun btnClick(view: View){
        val buSelected:Button = view as Button
        var cellId = 0
        when(buSelected.id){
            R.id.buttonA1 ->cellId = 1
            R.id.buttonA2 ->cellId = 2
            R.id.buttonA3 ->cellId = 3
            R.id.buttonA4 ->cellId = 4
            R.id.buttonA5 ->cellId = 5
            R.id.buttonB1 ->cellId = 6
            R.id.buttonB2 ->cellId = 7
            R.id.buttonB3 ->cellId = 8
            R.id.buttonB4 ->cellId = 9
            R.id.buttonB5 ->cellId = 10
            R.id.buttonC1 ->cellId = 11
            R.id.buttonC2 ->cellId = 12
            R.id.buttonC3 ->cellId = 13
            R.id.buttonC4 ->cellId = 14
            R.id.buttonC5 ->cellId = 15
            R.id.buttonD1 ->cellId = 16
            R.id.buttonD2 ->cellId = 17
            R.id.buttonD3 ->cellId = 18
            R.id.buttonD4 ->cellId = 19
            R.id.buttonD5 ->cellId = 20
            R.id.buttonE1 ->cellId = 21
            R.id.buttonE2 ->cellId = 22
            R.id.buttonE3 ->cellId = 23
            R.id.buttonE4 ->cellId = 24
            R.id.buttonE5 ->cellId = 25
            R.id.buttonF1 ->cellId = 26
            R.id.buttonF2 ->cellId = 27
            R.id.buttonF3 ->cellId = 28
            R.id.buttonF4 ->cellId = 29
            R.id.buttonF5 ->cellId = 30
            R.id.buttonG1 ->cellId = 31
            R.id.buttonG2 ->cellId = 32
            R.id.buttonG3 ->cellId = 33
            R.id.buttonG4 ->cellId = 34
            R.id.buttonG5 ->cellId = 35
            R.id.buttonH1 ->cellId = 36
            R.id.buttonH2 ->cellId = 37
            R.id.buttonH3 ->cellId = 38
            R.id.buttonH4 ->cellId = 39
            R.id.buttonH5 ->cellId = 40
            R.id.buttonI1 ->cellId = 41
            R.id.buttonI2 ->cellId = 42
            R.id.buttonI3 ->cellId = 43
            R.id.buttonI4 ->cellId = 44
            R.id.buttonI5 ->cellId = 45
            R.id.buttonJ1 ->cellId = 46
            R.id.buttonJ2 ->cellId = 47
            R.id.buttonJ3 ->cellId = 48
            R.id.buttonJ4 ->cellId = 49
            R.id.buttonJ5 ->cellId = 50
        }
        //Log.d("BuClick",buSelected.id.toString())
        //Toast.makeText(this@MainActivity,"${cellId}",Toast.LENGTH_SHORT).show()
        playGame(cellId,buSelected)
        check_winner(p1pts,p2pts,buSelected)
    }


    var roundCount = 0

    // PLAYERS
    var player1 = ArrayList<Int>()
    var player2 = ArrayList<Int>()

    //PLAYER BETS
    var p1pts:Int = 0
    var p2pts:Int = 0

    var random_mine = Random.nextInt(1..51)

    var mine:Boolean = false



    fun playGame(cellId:Int,buSelected:Button){
        var countRoundTXT: TextView? =findViewById<TextView>(R.id.turnCountTxt)
        var player1bet:TextView = findViewById<TextView>(R.id.player1bet)
        var player2bet:TextView = findViewById<TextView>(R.id.player2bet)
        if (activePlayer==1){
            roundCount.toInt().toString()
            countRoundTXT?.text = roundCount.toString()
            buSelected.text = (p1pts * 1000.0 / 100).roundToInt().toString()
            p1pts+=1
            p1pts.toInt().toString()
            player1bet.text =p1pts.toString()
            buSelected.setBackgroundColor(Color.BLUE)
            player1.add(cellId)
            roundCount+=1
            activePlayer=2
        } else if (activePlayer == 2 ){
            buSelected.text = "0.05"
            p2pts+=1
            p2pts.toInt().toString()
            player2bet.text =p1pts.toString()
            buSelected.setBackgroundColor(Color.RED)
            player2.add(cellId)
            activePlayer = 1
        }


        buSelected.isEnabled = false
    }

    /*fun set_mine(cellId: Int){
        var minebtn:Button = findViewById(R.id.setMineBtn)
        var mine1 = false
        var mine2 = false
        if (activePlayer == 1){
            minebtn.setOnClickListener{
                mine1 = true
            }
        } else if(activePlayer ==2){
            minebtn.setOnClickListener{
                mine2 = true
            }
        }


    }*/

    fun check_winner(p1pts:Int, p2pts:Int,buSelected:Button){
        var winner:Int = 0
        if (p1pts >=20 && p2pts<20){
            winner = 1
            buSelected.isEnabled = false
            Toast.makeText(this@MainActivity,"Player1 wins",Toast.LENGTH_LONG).show()
        } else if(p2pts >=20 && p1pts<20){
            winner = 2
            buSelected.isEnabled = false
            Toast.makeText(this@MainActivity,"Player1 wins",Toast.LENGTH_LONG).show()
        }
            

    }

}