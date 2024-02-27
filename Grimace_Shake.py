print("\n**********************************************\n")

print("Weather Branch\n")

#Import Libraries
import random
from time import sleep

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
        print("VRS has been enganged only allowing you to drive 50mph")
    elif weatherAlert == "blizardy":
        print("\nNational Weather Service has updated our alarm be 45 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        print("VRS has been enganged only allowing you to drive 40mph")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm be 10 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        print("VRS has been enganged only allowing you to drive 60mph")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm be 10 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        print("VRS has been enganged only allowing you to drive 50mph")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm be 5 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        print("VRS has been enganged only allowing you to drive 70mph")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm be 35 minutes because of the forecast of", weatherAlert,
            "weather conditions.")
        print("VRS has been enganged only allowing you to drive 45mph")
    else:
        print("\nNational Weather Service gives a forecast of", weatherAlert,"weather conditions.")
        print("VRS has not been enganged")



VRS()