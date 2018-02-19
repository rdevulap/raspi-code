from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()
count = 0
while True:
    count = count + 1
    now = datetime.datetime.now()
    dateandtime = now.strftime("%Y-%m-%d_%H:%M:%S")
    filename = "image_" + str(dateandtime) + "_" + str(count)
    print("taking picture", filename)
    sleep(300)
    camera.capture('/home/pi/rdevulap-raspi-code/raspi-code/data-collection/data/%s.jpg' % filename)
