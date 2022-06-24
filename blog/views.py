from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def search(request):
    city = request.GET['city']
    image_url = "http://openweathermap.org/img/wn/"
    url = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&units=metric&appid=934adaa7fb59ca72db3ef92c70582552"
    response = requests.get(url)
    jsonResponse = response.json()
    description = jsonResponse['weather'][0]['description']
    icon_code = jsonResponse['weather'][0]['icon']
    image_icon = image_url + icon_code + '.png'
    return render(request, 'blog/index.html', {'jsonResponse': jsonResponse, 'description': description, 'image_icon': image_icon})
