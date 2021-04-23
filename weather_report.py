import requests

def Weather(city_name):
    url='http://api.openweathermap.org/data/2.5/weather?appid=YOUR API KEY&q='
    url = url + city_name
    json_weather_data = requests.get(url).json()
    weather_main = json_weather_data['main']
    return weather_main