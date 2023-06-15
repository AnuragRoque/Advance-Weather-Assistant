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
    speak("I'm your personal weather assistant. Currently showing   complete weather information")
    speak("  And  if you need anything   Just ask")

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


async def getweatherfull():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find("Greater Noida")

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)
        #speak(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()



def tellDay():
      
    
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number 
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
  
  
def tellTime():
      
    # This method will give the time
    time = str(datetime.datetime.now())
      
    # the time will be displayed like 
    # this "2020-06-05 17:50:14.582630"
    #nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("Currently " + hour + "Hours and" + min + "Minutes") 

def tellTime2():
    
    from datetime import datetime
    print(datetime.today().strftime("%I:%M %p"))
    speak(datetime.today().strftime("It's %I:%M %p"))




def technews(): 
    #url='https://www.bbc.com/news'
    url='https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-IN&gl=IN&ceid=IN:en'
    #topnews=url='https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen'    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')

    timeout = time.time() + 60 
    for x in headlines:
        if time.time() > timeout:
            break
        print('=>')
        print(x.text.strip())
        speak(x.text.strip())
        """""
        commandnow()
        if 'stop' in query:
            speak('ok')
            break
        else:
            continue
    
        """
        #query=takecommand().lower()
        #if 'stop' in query:
        #    break

def topnews(): 
    #url='https://www.bbc.com/news'
    #tech=url='https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-IN&gl=IN&ceid=IN:en'
    url='https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen'    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')

    timeout = time.time() + 20 
    for x in headlines:
        if time.time() > timeout:
            break
        print('=>')
        print(x.text.strip())
        speak(x.text.strip())
    
def worldnews(): 
    #url='https://www.bbc.com/news'
    #tech=url='https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-IN&gl=IN&ceid=IN:en'
    url='https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')

    timeout = time.time() + 20 
    for x in headlines:
        if time.time() > timeout:
            break
        print('=>')
        print(x.text.strip())
        speak(x.text.strip())
def indianews(): 
    #url='https://www.bbc.com/news'
    #tech=url='https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-IN&gl=IN&ceid=IN:en'
    url='https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen'    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')

    timeout = time.time() + 20 
    for x in headlines:
        if time.time() > timeout:
            break
        print('=>')
        print(x.text.strip())
        speak(x.text.strip())
    
    
def dailynews():
    speak("Sir Do you want the Daily News ")
    query=takecommand().lower()
    if 'yes' in query:
        technews()
    elif 'no' in query:
        speak('ok')
def showtask():
    speak("No task assigned for today")

def todaytask():

    lst=["Do you want to checkout today's task sir?","let me remind you sir we have some tasks for today do you want to check them now or later"]
    random.shuffle(lst)
    for tasks in lst:
        #print tasks
        speak(tasks)
    #speak("Do you want to checkout today's task sir?")
    query=takecommand().lower()
    if 'yes' in query:
        showtask()
    elif 'no' in query:
        speak('ok')
    


            
  


def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 4
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.h
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query    

#extra
def search_web():
  
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()
  
    if 'youtube' in query:
  
        speak("Opening in youtube")
        indx = takecommand.lower().split().index('youtube')
        query=takecommand.split()[indx + 1:]
        #query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return
    else:
        speak("unable to find")





if __name__=="__main__" :
        loop = asyncio.get_event_loop()
        loop.run_until_complete(getweather())
        greetme()
        while True:
            query=takecommand().lower()    
            if 'wikipedia' in query:
                speak('Results from Wikipedia Sir!')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            
            elif 'temperature' in query:
                with open("C:\\Users\\anura\\Desktop\\putty.log","r") as f:
                    first_line=f.readline()
                    for line in f:
                        pass
                    last_line = line

                tempp=str(first_line)
                humm=str(last_line)
                speak(tempp)
            elif 'humidity' in query:
                with open("C:\\Users\\anura\\Desktop\\putty.log","r") as f:
                    first_line=f.readline()
                    for line in f:
                        pass
                    last_line = line

                tempp=str(first_line)
                humm=str(last_line)
                speak(humm)

            elif "which day it is" in query:
                tellDay()
            elif "today's day" in query:
                tellDay()            
            elif 'tell me the time' in query:
                tellTime()
            elif 'time right now' in query:
                tellTime()
            elif 'time' in query:
                tellTime()
            elif 'complete weather' in query:
                getweatherfull()
            elif 'yes' in query:
                speak("can you repeat? sir,")
            elif 'date' in query:
                x = datetime.datetime.now()
                print(x.date)
                speak(x.date)
            elif 'weather' in query:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(getweather())
            elif 'who are you' in query:
                speak("Hello Sir, I'm personal weather assistant i displays and tell complete weather information I am your morning star if you need anything Just ask")
            elif 'Introduce yourself'in query:
                speak("Hello Sir, I'm personal weather assistant i displays and tell complete weather information I am your morning star if you need anything Just ask")
            
            elif 'hello' in query:
                greetme()
                tellDay()
                
                
                dailynews()
            elif 'tech news' in query:
                technews()
            elif 'global news' in query:
                worldnews()
            elif 'top news' in query:
                topnews()
            elif 'india news' in query:
                indianews()
                

            elif 'stop' in query:
                exit()

            elif 'jarvis logout' in query:
                speak('sir ? sir? logging off sir')
                exit()

            elif 'hey jarvis' in query:
                speak("Yes Sir!! i'm here waht do you need")
            elif 'hey ladies' in query:
                speak('sir ? Are you kidding, i, am, not, your, ladies, sir!  give me some, respect! please?')