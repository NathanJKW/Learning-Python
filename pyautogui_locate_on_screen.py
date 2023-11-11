"""This is an example of using pyautogui to locat an image on the screen"""

import pyautogui

image_location = pyautogui.locateOnScreen('pyautogui_locate_on_screen.png', grayscale=True)

print(image_location)

location_center = pyautogui.center(image_location)

print(location_center)

pyautogui.moveTo(location_center.x, location_center.y, 2)
