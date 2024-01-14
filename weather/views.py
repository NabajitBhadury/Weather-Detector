from django.shortcuts import render
import json
import urllib.request
from urllib.error import HTTPError

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        querycity=city.replace(' ','+')
        try:
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+querycity+'&appid=f50e9976a4c58b87918d0c73485c31a6').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + '' + str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp']) + 'k',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }
        except HTTPError as e:
            data = {}
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city':city , 'data':data})
