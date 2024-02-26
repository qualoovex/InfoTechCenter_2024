print("\n**********************************************\n")

print("Weather Branch\n")

#Import Libraries
import random
from time import sleep

#Create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["snowy", "blizards", "rainy", "foggy", "windy", "icy", "sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Variable to call weather() once VRS(Vehicle Respoce System) is determined
weatherAlert = weather()

def VRS():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm be 30 minutes because of the forecast of", weatherAlert,
            "weather conditions.")

        print("VRS has been enganged only allowing you to drive 50mph")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm be 45 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        print("VRS has been enganged only allowing you to drive 40mph")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm be 10 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        print("VRS has been enganged only allowing you to drive 60mph")
    




VRS()