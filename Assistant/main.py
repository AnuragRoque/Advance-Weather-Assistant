from flask import Flask,render_template, url_for
from ssl import ALERT_DESCRIPTION_UNRECOGNIZED_NAME

import time
import datetime
import os
import python_weather
import asyncio
import requests
from bs4 import BeautifulSoup

app=Flask(__name__,template_folder='template')
timeex = time.strftime("%Y-%m-%d  %H:%S")
timee = time.strftime("%H:%S")
datee=time.strftime("%Y-%m-%d")




@app.route("/")
def home():
    
    #y=str(getweather())
    

    with open("C:\\Users\\anura\\Desktop\\putty.log","r") as f:
        first_line=f.readline()
        for line in f:
            pass
        last_line = line
    tempp=str(first_line)
    humm=str(last_line)

    


    
    return render_template('weather.html',  timee=timee,datee=datee,temp=tempp,humm=humm)
    
    
    


if __name__ == '__main__':
        
    app.run(debug=True)
    
    

   