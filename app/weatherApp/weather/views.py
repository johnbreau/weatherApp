from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from .models import City
from .forms import CityForm
# from .forms import DeleteForm
from django.http import HttpResponseRedirect

def index(request):
        cities = City.objects.all() 
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=fdcf9e40f8e2bed200c2a46856a44335'
        
        if request.method == 'POST': # only true if form is submitted
            print('hello1')
            form = CityForm(request.POST) # add actual request data to form for processing
            form.save() # will validate and save if validate
            return HttpResponseRedirect('./')
        form = CityForm()

        if request.method == 'DELETE': # only true if form is submitted
            
            # form = DeleteForm(request.DELETE) # add actual request data to form for processing
            # form.save() # will validate and save if validate
            return HttpResponseRedirect('./')
    
        weather_data = []
        for city in cities:
            city_weather = requests.get(url.format(city)).json()

            weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
            }
        
            weather_data.append(weather)
        context = {'weather_data' : weather_data, 'form' : form}
        return render(request, 'index.html', context)

    
