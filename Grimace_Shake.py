print("*********************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random
from time import sleep

#Function that lists gas levels. randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#function that lists gas stations, random;y choosing one and returning its value

def listOfGasStations():
    gasStations = ["Shell", "SpeedWay", "Marathon", "CricleK", "Mobile", "Costco", "Meijer", "Kum & Go"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

#Function will call the gas level gage functino to determin our gas level and then fine a close gas
# station if we are on by calling the list of gasStations function if we are on low or quarter tank
def gasLevelAlert():
    milesTGSLow = round(random.uniform(1, 25),1)
    milesTGSQuater = round(random.uniform(25.1, 50),1)
    gasLevel = gasLevelGauge()
    if gasLevel == "Empty":
        print ("***WARNING - YOU ARE ON EMPTY***")
        sleep(2.5)
        print("***Calling Triple AAA***")
    elif gasLevel== "Low":
        print("Your gas tank is EXTREMLY low, checking google maps for the closest gas station...")
        sleep (2.5)
        print("The closest gasstation is,",listOfGasStations(),"which is",milesTGSLow,"miles away." )
    elif gasLevel== "Quarter Tank":
        print("Your gas tank is at a Quarter tank, checking google maps for gas stations nearby...")
        sleep (2.5)
        print("The closest gasstation is,",listOfGasStations(),"which is",milesTGSQuarter,"miles away." )
    elif gasLevel== "Half Tank":
        print("Your gas tank is at a half tank, which is plent to get to fet to your destination.")
    elif gasLevel== "Three Quarter Tank":
        print("Your gas tank is at three quarters of a tank, which is more than enough to get to your destination.")
    else:
        print("Your gas tank is full!")




gasLevelAlert()



