import pyautogui 
import keyboard


while True:
    if keyboard.is_pressed("s"):
        pyautogui.doubleClick()
    if keyboard.is_pressed("q"):
        break