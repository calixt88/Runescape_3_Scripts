import random
import pyautogui
import time


def main():
    start_screen()
    check_mouse_position()
    look_north()
    mining()


def mining():
    time.sleep(1)
    pyautogui.moveTo(848, 664)

    for i in range(1000):
        print("Click")
        print(i)
        pyautogui.click()
        quick_sleep()
        check_mouse_position()


def check_mouse_position():
    currentMouseX, currentMouseY = pyautogui.position()
    if currentMouseX != 848 & currentMouseY != 664:
        pyautogui.moveTo(848, 664)
    else:
        print(currentMouseX, currentMouseY, "Correct Position")


def look_north():
    pyautogui.moveTo(1393, 88)
    pyautogui.click()


def quick_sleep():
    time.sleep(random.uniform(2, 6))


def start_screen():
    input("Hit the Enter button to start the script")
    print("\nBooting Up...")
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)


main()
