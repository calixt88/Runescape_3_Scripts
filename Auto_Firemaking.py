import random
import pyautogui
import time
import Script_Imports


def main():
    Script_Imports.start_screen()
    Script_Imports.look_north()
    for i in range(40):
        firemaking()


def firemaking():
    Script_Imports.look_north()
    pyautogui.moveTo(871, 904)
    time.sleep(1)
    pyautogui.click()
    time.sleep(random.uniform(60, 75))
    pyautogui.moveTo(1070, 751)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.keyDown('1')
    pyautogui.keyUp('1')
    time.sleep(1)


main()