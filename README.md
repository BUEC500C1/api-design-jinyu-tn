# api-design-jinyu-tn
api-design-jinyu-tn created by GitHub Classroom

## Project target:
1. Show which city the airport is by the data from the file *airports.csv*.
2. Use  *OpenWeatherMAP API*  to get current weather of this city.

## User story:
* As a traveler, I want to know the current weather of the airport so that I can know whether my flight will be canceled.
* As a stuff of a company, I want to know the weather of the airport so that I can book appropriate tickets for my boss.
* As a uber driver, I want to know whether the airport is rainning so that I can know if I can get more orders.

## Module description：

### Input and output module:
User type in the airport name from the user interface, and our api print out the result to the user interface.
### Data Management module
- The function **codetoname(airportname)** in the file `currentweather.py`covert airport name to corresponding city name with the data of file `airports.csv`.
- The **main function** of the file `currentweather.py`use *OpenWeatherMAP API* and city name to get the weather data of the city.
- The function **print_current_weather(data)** in the file `currentweather.py`filters the weather data we need and print it out.
