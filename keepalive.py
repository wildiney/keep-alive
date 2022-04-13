import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = False

numMin = 1

if((len(sys.argv) < 2) or sys.argv[1].isalpha() or int(sys.argv[1]) < 1):
    numMin = 1
else:
    numMin = int(sys.argv[1])

try:
    x = 0
    while(x < numMin):

        time.sleep(20)
        mouseposition = pyautogui.position()
        x += 1

        for i in range(0, 100):
            pyautogui.moveTo(i*4, i*4)
            time.sleep(.25)
            # print("move to "+str(i))
        pyautogui.moveTo(mouseposition)
        for i in range(0, 3):
            pyautogui.press("shift")
            # print("press shift")
        print("Movement made at {}".format(datetime.now().time()))
except KeyboardInterrupt:
    print("Execution finished!")
