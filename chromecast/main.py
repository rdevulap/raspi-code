from __future__ import print_function
from time import sleep
import datetime
import time
import pychromecast

time1 = time.time()
chromecasts = pychromecast.get_chromecasts()
time2 = time.time()
print('function took', (time2-time1)*1000.0, 'ms')
print(chromecasts)
