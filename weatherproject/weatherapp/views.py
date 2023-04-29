from django.shortcuts import render
import requests
# Create your views here.
from django.shortcuts import render
import requests


def index(request):
    api_key = '124fef7ad1582d2c35bbccfe727eb626'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    if request.method == 'POST':
        city = request.POST['city']
        weather_data1= fetch_weather(city, api_key, current_weather_url)
        context = {
            'weather_data1': weather_data1,

        }

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def fetch_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'humidity':response['main']['humidity'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }
    return weather_data