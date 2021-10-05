import time

import pyautogui


def look_north():
    pyautogui.moveTo(1393, 88)
    pyautogui.click()


def start_screen():
    input("Hit the Enter button to start the script")
    print("\nBooting Up...")
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)


def check_mouse_position():
    screenWidth, screenHeight = pyautogui.size()
    print(screenWidth, screenHeight)