print("*********************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random

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


print(gasLevelGauge())
print(listOfGasStations())


