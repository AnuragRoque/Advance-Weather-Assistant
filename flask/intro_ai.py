#import audioop
import pyttsx3
import webbrowser
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import time
#import keys
#import convo
import python_weather
import asyncio
import requests
from bs4 import BeautifulSoup
import random
#extra
from selenium import webdriver





#import brian2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# Set Rate
#engine.setProperty('rate', 190)
# Set Volume
#engine.setProperty('volume', 1.0)
# Set Voice (Female)

#brian2.test()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def speak2(audio):
    engine.say(audio)
    engine.runAndWait()




def greetme():
   
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon Sir")
    elif hour >= 16 and hour < 19:
        speak("Good Evening Sir ")
        
   
        
    #speak("I am Not Jarvis. How may I assist you Sir!!")
    #speak("Sir!!")
def intro():
    speak("I'm your personal weather assistant. Currently showing complete weather information")
    speak("And if you need anything Just ask")

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find("Greater Noida")

    # returns the current day's forecast temperature (int)
    x=print(weather.current.temperature)
    speak("The Weather in Grater Noida is")
    speak(weather.current.temperature)
    speak("degree celcius")
    

    # get the weather forecast for a few days
    

    # close the wrapper once done
    await client.close()




if __name__=="__main__" :
    greetme()
    speak("Hello Sir,   I am your  personal weather assistant. How may i help you.  if you need anything, Just ask")
    

    