import pyautogui as pyg
import time

for i in range(5):
    time.sleep(5)
    pyg.write("I love Python",interval=0.25)
    pyg.press("enter")