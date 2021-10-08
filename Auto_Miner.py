import random
import pyautogui
import time
import Script_Imports


def main():
    start = time.time()
    Script_Imports.start_screen()
    # correct_mouse_position()
    Script_Imports.look_north()
    mining()
    end = time.time()
    print(end - start)


def mining():
    time.sleep(1)
    pyautogui.moveTo(848, 664)

    for i in range(1050):
        print("Click")
        print(i)
        pyautogui.click()
        quick_sleep()
        correct_mouse_position()


def correct_mouse_position():
    currentMouseX, currentMouseY = pyautogui.position()
    if currentMouseX != 848 & currentMouseY != 664:
        pyautogui.moveTo(848, 664)
    else:
        print(currentMouseX, currentMouseY, "Correct Position")


def quick_sleep():
    time.sleep(random.uniform(2, 6))


main()
