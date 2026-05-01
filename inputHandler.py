import threading
import queue
import time

commands = queue.Queue()
running = True
enabled = True

def _input_loop():
    global running, enabled
    while running:
        if enabled:
            cmd = input("\n> ")
            commands.put(cmd)
        else:
            time.sleep(0.05)

def startInputThread():
    thread = threading.Thread(target=_input_loop, daemon=True)
    thread.start()

def getCommand():
    if not commands.empty():
        return commands.get().lower().strip()
    return ""

def pause():
    global enabled
    enabled = False

def resume():
    global enabled
    enabled = True