


#Import Libraries here

import time
import sys
import random
from time import sleep

#Welcome-branch starts here
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
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!\n")
#gasoline branch starts here
print("*********************************\n")
print("Gasoline Branch\n\n")




#Function that lists gas levels. randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#function that lists gas stations, randomly choosing one and returning its value

def listOfGasStations():
    gasStations = ["Shell", "SpeedWay", "Marathon", "CircleK", "Mobile", "Costco", "Meijer", "Kum & Go"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

#Function will call the gas level gage functinon to determine our gas level and then fine a close gas
# station if we are on by calling the list of gasStations function if we are on low or quarter tank
def gasLevelAlert():
    milesTGSLow = round(random.uniform(1, 25),1)
    milesTGSQuater = round(random.uniform(25.1, 50),1)
    gasLevel = gasLevelGauge()
    if gasLevel == "Empty":
        print ("***WARNING - YOU ARE ON EMPTY***")
        sleep(2.5)
        print("***Calling Triple AAA***")
    elif gasLevel == "Low":
        print("Your gas tank is EXTREMELY low, checking google maps for the closest gas station...")
        sleep (2.5)
        print("The closest gas station is,",listOfGasStations(),"which is",milesTGSLow,"miles away." )
    elif gasLevel == "Quarter Tank":
        print("Your gas tank is at a Quarter tank, checking google maps for gas stations nearby...")
        sleep (2.5)
        print("The closest gas station is,",listOfGasStations(),"which is",milesTGSQuater,"miles away." )
    elif gasLevel == "Half Tank":
        print("Your gas tank is at a half tank, which is plenty to get to fet to your destination.")
    elif gasLevel == "Three Quarter Tank":
        print("Your gas tank is at three quarters of a tank, which is more than enough to get to your destination.")
    else:
        print("Your gas tank is full!")




gasLevelAlert()




#Weather starts here
print("\n*********************************\n")

print("Weather Branch")


#Create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["snowy", "blizardy", "rainy", "foggy", "windy", "icy", "sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Variable to call weather() once VRS(Vehicle Respoce System) is determined
weatherAlert = weather()

def VRS():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm be 30 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        sleep(1)
        print("VRS has been enganged only allowing you to drive 50mph")
    elif weatherAlert == "blizardy":
        print("\nNational Weather Service has updated our alarm be 45 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        sleep(1)
        print("VRS has been enganged only allowing you to drive 40mph")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm be 10 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        sleep(1)
        print("VRS has been enganged only allowing you to drive 60mph")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm be 10 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        sleep(1)
        print("VRS has been enganged only allowing you to drive 50mph")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm be 5 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        sleep(1)
        print("VRS has been enganged only allowing you to drive 70mph")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm be 35 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        sleep(1)
        print("VRS has been enganged only allowing you to drive 45mph")
    else:
        print("\nNational Weather Service gives a forecast of", weatherAlert,"weather conditions.")
        sleep(1)
        print("VRS has not been enganged")



VRS()

