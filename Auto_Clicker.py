import time
from random import uniform
import pyautogui
import Script_Imports


def main():
    Script_Imports.start_screen()
    clicker()


def clicker():
    for i in range(2000):
        pyautogui.click()
        time.sleep(uniform(0.9, 2.3))
        print("Click ", i)


main()
