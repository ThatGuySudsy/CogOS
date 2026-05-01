import shutil
import os
import settingsApp
import state

borderStyles = [
    {
    "tl": "+", "tr": "+",
    "bl": "+", "br": "+",
    "h": "-", "v": "|"
},
    {
    "tl": "┌", "tr": "┐",
    "bl": "└", "br": "┘",
    "h": "─", "v": "│"
},
    {
    "tl": "┏", "tr": "┓",
    "bl": "┗", "br": "┛",
    "h": "━", "v": "┃"
},
    {
    "tl": "╔", "tr": "╗",
    "bl": "╚", "br": "╝",
    "h": "═", "v": "║"
},
    {
    "tl": "╭", "tr": "╮",
    "bl": "╰", "br": "╯",
    "h": "─", "v": "│"
}]

width = shutil.get_terminal_size().columns
height = shutil.get_terminal_size().lines

def border(selected):
    return borderStyles[settingsApp.loadSetting(state.username, "borderStyle")][selected]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def appBar(appName):
    print(border("tl") + (border("h") * (width - 2)) + border("tr"))
    print(border("v") + (" " * (width - 2)) + border("v"))
    print(border("v") + appName + (" " * (width - 2 - len(appName))) + border("v"))
    print(border("v") + (" " * (width - 2)) + border("v"))
    print(border("bl") + (border("h") * (width - 2)) + border("br"))
    print()

def loading(percent):
    clear()
    print("   _____             ____   _____ ".center(width))
    print("  / ____|           / __ \ / ____|".center(width))
    print(" | |     ___   __ _| |  | | (___  ".center(width))
    print(" | |    / _ \ / _` | |  | |\___ \ ".center(width))
    print(" | |___| (_) | (_| | |__| |____) |".center(width))
    print("  \_____\___/ \__, |\____/|_____/ ".center(width))
    print("               __/ |              ".center(width))
    print("              |___/               ".center(width))
    print()
    print()
    filled = int(percent / 5)
    bar = "=" * filled + "-" * (20 - filled)
    print(f"[{bar}] {percent}%".center(width))
   
def user():
    clear()
    print("            ......            ".center(width))
    print("        ::::::::::::::.       ".center(width))
    print("     .::::::::--::::::::.     ".center(width))
    print("    :::::::-======-:::::::    ".center(width))
    print("  .:::::::==========:::::::.  ".center(width))
    print(" .::::::::==========::::::::. ".center(width))
    print(" :::::::::-========-::::::::: ".center(width))
    print(" ::::::::::-======-:::::::::: ".center(width))
    print(" :::::::::::::::::::::::::::: ".center(width))
    print(" :::::::::---====---::::::::: ".center(width))
    print(" .:::::-==============-:::::. ".center(width))
    print("  .::-==================-::.  ".center(width))
    print("   .======================.   ".center(width))
    print("     :==================:     ".center(width))
    print("       .:============:.       ".center(width))
    print("           .::::::.           ".center(width))
        
        
def desktop(time, date):
    print(border("tl") + (border("h") * (width - 2)) + border("tr"))
    print(border("v") + (" " * (width - 2)) + border("v"))
    print(border("v") + "CogOS v0.0.1" + (" " * (width - 14)) + border("v"))
    print(border("v") + (" " * (width - 2)) + border("v"))
    print(border("bl") + (border("h") * (width - 2)) + border("br"))
    print()
    print("[0] Clock".center(width))
    print("[1] Calc ".center(width))
    print()
    for lines in range (height-11 ): print()
    print(f"CogOS {time} {date} [q] Quit")

def pushNotification(title):
    print("--------------------")
    print("|" + title + (" " * (18 - len(title)) + "|"))
    print("--------------------")

#------------------------------------------- Clock App -------------------------------------------

def clockMain(date, time):
    appBar("Clock")
    print("[Clock] | Stopwatch | Alarm | Timer".center(width))
    print()
    print(date.center(width))
    print(time.center(width))

def clockStopwatch(time, isOn):
    appBar("Clock")
    print("Clock | [Stopwatch] | Alarm | Timer".center(width))
    print()
    print(str(round(time, 2)).center(width))
    print(((" Stop" if isOn else "Start") + "[0] | Reset [1]").center(width))

def clockTimer(time, isOn):
    appBar("Clock")
    print("Clock | Stopwatch | Alarm | [Timer]".center(width))
    print(time)
    print(("Start [0]" if isOn else "Cancel [0]"))
    
#------------------------------------------- Calculator App -------------------------------------------

def calcMain(equation, answer):
    appBar("Calculator")
    print(("-" * (width - len(equation) - 2)) + equation + ("--"))
    print("|" + answer + (" " * (width - len(answer) - 2)) + "|")
    print(("-" * (width)))
    print()
    print("+---+ +---+ +---+  |  +---+".center(width))
    print("| 7 | | 8 | | 9 |  |  | / |".center(width))
    print("+---+ +---+ +---+  |  +---+".center(width))
    print("                   |       ".center(width))
    print("+---+ +---+ +---+  |  +---+".center(width))
    print("| 4 | | 5 | | 6 |  |  | * |".center(width))
    print("+---+ +---+ +---+  |  +---+".center(width))
    print("                  |       ".center(width))
    print("+---+ +---+ +---+  |  +---+".center(width))
    print("| 1 | | 2 | | 4 |  |  | - |".center(width))
    print("+---+ +---+ +---+  |  +---+".center(width))
    print("                   |       ".center(width))
    print("      +---+        |  +---+".center(width))
    print("      | 0 |        |  | + |".center(width))
    print("      +---+        |  +---+".center(width))