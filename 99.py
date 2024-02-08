# ************************  Desktop Notification System for Ubuntu  ************************

import os
import time


duration  = int(input("Enter the duration after which you want to show notification: "))

time.sleep(duration)

os.system('notify-send -i face-wink "Smile please"')  # This will display a notification on your desktop
