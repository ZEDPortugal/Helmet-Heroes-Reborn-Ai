import tkinter as tk
import threading
import pydirectinput
import time
import winsound

def start_loop():
    global is_running
    is_running = True
    threading.Thread(target=countdown).start()

def stop_loop():
    global is_running
    is_running = False

def countdown():
    for i in range(3, 0, -1):
        winsound.Beep(1000, 500)
        time.sleep(1)
    run_loop()

def run_loop():
    while is_running:
        pydirectinput.keyDown('space')
        time.sleep(5)
        pydirectinput.keyUp('space')
        pydirectinput.keyDown('d')
        pydirectinput.keyDown('e')
        time.sleep(9)
        pydirectinput.keyUp('d')
        pydirectinput.keyUp('e')
        pydirectinput.keyDown('a')
        pydirectinput.keyDown('space')
        time.sleep(9)
        pydirectinput.keyUp('space')
        pydirectinput.keyDown('a')
        pydirectinput.keyDown('e')
        time.sleep(9)
        pydirectinput.keyUp('a')
        pydirectinput.keyUp('e')
        pydirectinput.keyDown('d')
        pydirectinput.keyUp('d')

def create_ui():
    root = tk.Tk()
    root.configure(bg='black')

    start_button = tk.Button(root, text="Start", command=start_loop, bg='gray', fg='white')
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop", command=stop_loop, bg='gray', fg='white')
    stop_button.pack(pady=10)

    root.mainloop()

is_running = False
create_ui()
