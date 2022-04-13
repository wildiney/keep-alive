import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = False

def main():
    is_mouse_idle()


def is_mouse_idle():
    last_position = None
    time_idle = 0
    cycle = 60
    max_time_idle = 5

    while(True):
        time.sleep(cycle)
        position = pyautogui.position()
        if(position == last_position):
            print("{}".format(datetime.now().time()))
            time_idle += 1
            if(time_idle > max_time_idle):
                print("Running")
                for i in range(0, 15):
                    pyautogui.moveTo(i*4, i*4)

                for i in range(0, 3):
                    pyautogui.press("shift")

                pyautogui.moveTo(last_position)
        else:
            last_position = position
            time_idle = 0


try:
    while(True):
        print("START")
        main()
except KeyboardInterrupt:
    print("Finished")

if __name__ == "__main__":
    main()
