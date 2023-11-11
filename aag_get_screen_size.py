"""Examples of getting screen size."""

#conda install pyautogui

import pyautogui

size = pyautogui.size()

width = size.width

height = size.height

print(size)
print(width)
print(height)
