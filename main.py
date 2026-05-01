import render
from time import sleep
import clockApp
import calculatorApp
import settingsApp
import inputHandler
import userManager
import state

page = "desktop"
subpage = ""

for i in range (101):
    (render.loading(i))
    sleep(0.01)

while True:
    render.user()
    state.username = input("Enter Username: ")
    match userManager.login(state.username, input("Enter Password: ")):
        case 0:
            print("WELCOME BACK")
            sleep(0.5)
            break
        case 1:
            print("NICE TO MEET YOU")
            sleep(0.5)
            break
        case 2:
            print("WRONG PASSWORD")
            sleep(0.5)

inputHandler.startInputThread()

while True:
    inp = inputHandler.getCommand()
    render.clear()

    if clockApp.timerEnd != 0:
        if clockApp.checkTimer() == "Not On":
            render.pushNotification("Timer Over")

    if page == "desktop":
        render.desktop(clockApp.time(settingsApp.loadSetting(state.username, "12HourTime")), clockApp.shortDate())
        if inp == "0":
            page = "clock"
            subpage = "main"
        if inp == "1":
            page = "calc"
            subpage = "main"
        elif inp == "t":
            render.pushNotification("Test Notification")
        elif inp == "q":
            inputHandler.running = False
            render.clear()
            break

    elif page == "clock":
        if subpage == "main":
            render.clockMain(clockApp.fullDate(), clockApp.time(settingsApp.loadSetting(state.username, "12HourTime")))
            if inp == "]":
                subpage = "stopwatch"
            elif inp == "[":
                subpage = "timer"
        elif subpage == "stopwatch":
            render.clockStopwatch(clockApp.stopwatchTime(), clockApp.stopwatchIsOn)
            if inp == "]":
                subpage = "alarm"
            elif inp == "[":
                subpage = "main"
            elif inp == "0":
                if clockApp.stopwatchIsOn:
                    clockApp.stopStopwatch()
                else:
                    clockApp.startStopwatch()
            elif inp == "1":
                clockApp.resetStopwatch()
        elif subpage == "timer":
            render.clockTimer(clockApp.checkTimer(), True if clockApp.timerEnd == 0 else False)
            if inp == "]":
                subpage = "main"
            elif inp == "[":
                subpage = "alarm"
            elif inp == "0":
                if clockApp.timerEnd == 0:
                    inputHandler.pause()
                    clockApp.startTimer()
                    inputHandler.resume()
                else:
                    clockApp.cancelTimer()
    elif page == "calc":
        if subpage == "main":
            inputHandler.pause()
            inp = input()
            render.calcMain(inp, str(calculatorApp.basicCalc(list(inp))))
            inputHandler.resume()
    
    if inp == "q":
        page = "desktop"
        subpage = ""
            
        

    sleep(0.05)