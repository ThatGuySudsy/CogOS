from datetime import datetime as dt
import time as t

stopwatchStart = 0
stopwatchOffset = 0
stopwatchIsOn = False

timerEnd = 0

def time(type):
    if type == True:
        return dt.now().strftime("%I:%M:%S %p")
    else:
        return dt.now().strftime("%H:%M:%S")

def fullDate():
    return dt.now().strftime("%B %D, %Y")

def shortDate():
    return dt.now().strftime("%x")

def weekday():
    return dt.now().strftime("%A")

def startStopwatch():
    global stopwatchIsOn, stopwatchStart
    if not stopwatchIsOn:
        stopwatchIsOn = True
        stopwatchStart = t.perf_counter()
    
def stopStopwatch():
    global stopwatchIsOn, stopwatchOffset
    if stopwatchIsOn:
        stopwatchOffset += t.perf_counter() - stopwatchStart
        stopwatchIsOn = False

def resetStopwatch():
    global stopwatchStart, stopwatchOffset, stopwatchIsOn
    stopwatchStart = t.perf_counter()
    stopwatchOffset = 0
    stopwatchIsOn = False

def stopwatchTime():
    if stopwatchIsOn:
        return stopwatchOffset + (t.perf_counter() - stopwatchStart)
    return stopwatchOffset

def startTimer():
    global timerEnd
    timerEnd = t.perf_counter()+ int(input("Enter Timer Duration in Seconds: "))
    
def cancelTimer():
    global timerEnd
    timerEnd = 0

def checkTimer():
    global timerEnd
    if timerEnd - t.perf_counter() <= 0:
        timerEnd = 0
        return "Not On"
    return round(timerEnd - t.perf_counter(), 2)