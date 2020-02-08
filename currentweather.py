#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:45:41 2020

@author: taimaame
"""

import requests 
import csv


#get the columns of the airport names and the city names

def codetoname(airportname):
    with open('/Users/taimaame/bu/2020Spring/EC500/airports.csv','r+') as csvfile:
        reader = csv.reader(csvfile)
        name_column = [row[3] for row in reader]
    with open('/Users/taimaame/bu/2020Spring/EC500/airports.csv','r+') as csvfile:
        reader = csv.reader(csvfile)    
        city_column = [row[10] for row in reader]
    
    index = name_column.index(airportname)
    city = city_column[index]
    print('The airport is at',city,'.')
    return city

def print_current_weather(data):
    temp = data['main']
    print('Current humidity :',temp['humidity'])
    print('Current temperature :',temp['temp'],',feels like :',temp['feels_like'])
    print('Maximum temperature :',temp['temp_max'],',minimum temperature :',temp['temp_min'])
    wind = data['wind']
    print('The degree of wind:',wind['deg'])
    weather = data['weather']
    print('Description of the weather :',weather[0]['description'])
    

def main():
    airportname = input('Enter your airport name : ') 
    city = codetoname(airportname)
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=ae031c0e20dd02f8f26bd97e20697016'.format(city)
    res = requests.get(url)
    data = res.json()
    print_current_weather(data)

if __name__ == '__main__':
    main()





