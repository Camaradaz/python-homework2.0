# Automatización de Chrome Dino
import pyautogui
import time

x_coor = 340
y_coor = 315
contador = 1

while True:
    if pyautogui.pixel(x_coor, y_coor)[0] != 32:
        print(f'Salto #{str(contador)}')
        pyautogui.press('space')
        time.sleep(0.1)
        contador +=1