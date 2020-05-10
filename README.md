# api-design-jinyu-tn
api-design-jinyu-tn created by GitHub Classroom

## Project target:
1. Show which city the airport is by the data from the file *airports.csv*.
2. Use  *OpenWeatherMAP API*  to get current weather of this city：https://openweathermap.org/

## User story:
* As a traveler, I want to know the current weather of the airport so that I can know whether my flight will be canceled.
* As a stuff of a company, I want to know the weather of the airport so that I can book appropriate tickets for my boss.
* As a uber driver, I want to know whether the airport is rainning so that I can know if I can get more orders.

## Install instructions:
1. Clone my repository:
`https://github.com/BUEC500C1/api-design-jinyu-tn.git`
2. Install Library:
`pip install requests`

## Module description：

### Input and Output Module:

* Input: Go to the *currentweather.py* and change the input of getweather() under *if __name__ == '__main__':*
 `getweather("Airport Name")`
 
* Input examples:

`getweather("Kitchen Creek Helibase Heliport")`

`getweather("Bailey Generation Station Heliport")`

* Output: I just simplified the output, it contains the 'The airport is at which city', 'Current humidity','Current temperature','Maximum temperature','minimum temperature','The degree of wind'and 'Description of the weather'.

* Output examples:
`('The airport is at', 'Chesterton', '.')`
`('Current temperature :', 284.57, ',feels like :', 278.46)`
`('Maximum temperature :', 285.37, ',minimum temperature :', 283.71)`
`('The degree of wind:', 230)`
`('Description of the weather :', u'clear sky')`

### Data Management Module
- The function **codetoname(airportname)** in the file `currentweather.py`covert airport name to corresponding city name with the data of file `airports.csv`.
- The **main function** of the file `currentweather.py`use *OpenWeatherMAP API* and city name to get the weather data of the city, data is gotten with **JSON** format，using the python library **requests** .
- The function **print_current_weather(data)** in the file `currentweather.py`filters the weather data we need and print it out.
### Error Check Module:
- File `test_currentwearther.py` checkes the accurence of this API, using **pytest**.


### OpenWeatherMap API:
#### [The URL of the API](https://openweathermap.org/current)
- Access current weather data for any location including over 200,000 cities.
- Current weather is frequently updated based on global models and data from more than 40,000 weather stations.
- Data is available in JSON, XML, or HTML format.

## Project Demo:

### Case 1:
![case1](https://github.com/BUEC500C1/api-design-jinyu-tn/blob/master/case1.png)
![case1result](https://github.com/BUEC500C1/api-design-jinyu-tn/blob/master/case1result.png)

### Case 2:
![case2](https://github.com/BUEC500C1/api-design-jinyu-tn/blob/master/case2.png)
![case2result](https://github.com/BUEC500C1/api-design-jinyu-tn/blob/master/case2result.png)
### Pytest result:
![pytest](https://github.com/BUEC500C1/api-design-jinyu-tn/blob/master/pytest.png)
