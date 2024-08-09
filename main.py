import pyautogui
import time


def skip():
    try:
        some_image = pyautogui.locateCenterOnScreen('some_image.png', confidence=.8)
        time.sleep(.25)
        if some_image:
            pyautogui.moveTo(full_img_hbo)
            pyautogui.click()
            print('Back to fullscreen!')
        
    except ImageNotFoundException:
        print('OSError Excepted')
        time.sleep(.25)


while True:
    skip()

