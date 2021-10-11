import pyautogui
import Script_Imports
import time
import random


def main():
    Script_Imports.start_screen()
    pyautogui.moveTo(1540, 88)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)

    for i in range(1):
        mine_luminite()
        pyautogui.moveTo(1535, 1050)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
    bank()


def mine_luminite():
    for j in range(3):
        pyautogui.moveTo(849, 698)
        pyautogui.click()
        time.sleep(random.uniform(1.7, 3.3))


def bank():
    print("Banking...")
    pyautogui.moveTo(1619, 325)
    time.sleep(1)
    pyautogui.click()
    time.sleep(20)
    pyautogui.press('d')
    time.sleep(1)
    pyautogui.moveTo(983, 256)
    time.sleep(2)
    pyautogui.click(button='right')
    pyautogui.moveTo(995, 290)
    time.sleep(2)
    pyautogui.click()
    time.sleep(20)
    pyautogui.moveTo(1540, 88)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(1705, 724)
    time.sleep(1)
    pyautogui.click()


main()
