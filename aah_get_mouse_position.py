"""Examples of getting mouse position."""

#conda install pyautogui

import pyautogui

position = pyautogui.position()

x = position.x

y = position.y

print(position)
print(x)
print(y)
