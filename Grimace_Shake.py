
#Import Libraries here

import time
import sys

timeToSleep = 1

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)


#Code to have the ellipsis add a dot every .5 seconds

x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center Operating System Loading" + "." * ellipsis)
    ellipsis = ellipsis + 1 
    sys.stdout.write("\r" + message)
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis= 0
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Gratned!")
