from django.shortcuts import render, redirect
import requests

def index(request):
    responses = None
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=7ef376a8726318e8e013b5a1ed40797b'

    if request.method == "POST":
        city = request.POST.get("city")
        if city:
             request.session['city']=city
        return redirect('index')
    
    city = request.session.get('city')
    if city:
        result = requests.get(url.format(city))
        if result.status_code == 200:
            responses = result.json()
        else:
            responses= {'error': 'City not found'}

    return render(request, "index/index.html", {'res':responses})
