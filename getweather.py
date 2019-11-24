#-*- coding:utf-8 -*-

import urllib.request
import json

def PohangWeather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Pohang&appid=643a770010b9a5b1787e9779695157e4'
    u = urllib.request.urlopen(url)
    data = u.read()

    j=json.loads(data)
    weather = j["weather"]
    temp =weather[0]
    id = temp["id"]

    if((500 <= id < 600) or (300<=id<400)):
        return "비"

    elif(600 <= id < 700):
        return "눈"

    elif((800 <= id < 900) or (700<=id<800)):
        if(id== 800):
            return "맑음"
        else:
           return "구름 낌"

    elif((200<=id<300) or (900 <= id <1000)): #토네이도, 태풍, 허리케인, 폭염, 폭설 등의 상황, 외식상황에는 적절치 않은듯
        return "극한 상황"

    else:
        return "기타" #Additional로 날씨정보로써의 가치가 크지 않다고 판