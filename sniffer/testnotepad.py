#you will need the win32 libraries for this snippet of code to work, Links below
import win32gui
from time import sleep
from pynput.keyboard import Key,Controller
keyboard = Controller()

#[hwnd] No matter what people tell you, this is the handle meaning unique ID, 
#["Notepad"] This is the application main/parent name, an easy way to check for examples is in Task Manager
#["test - Notepad"] This is the application sub/child name, an easy way to check for examples is in Task Manager clicking dropdown arrow
#hwndMain = win32gui.FindWindow("Notepad", "test - Notepad") this returns the main/parent Unique ID
hd=win32gui.FindWindow(None,'sniper')
sleep(5)
while True:    
    win32gui.SetForegroundWindow(hd)
    keyboard.press(keyboard._KeyCode(115))
    keyboard.release(keyboard._KeyCode(115))
    sleep(222)