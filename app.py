from flask import Flask, request, render_template
import requests
import geocoder
from geopy.geocoders import Nominatim
from datetime import datetime


app = Flask(__name__)

# initialize api
geolocator = Nominatim(user_agent="geoapiExercises")

@app.route("/")
def index():
    city, country, temp = get_location()
    time = get_time()
    return render_template('index.html', city=city, country=country, temp=temp, time=time)




def get_location():
    api_key = "30d4741c779ba94c470ca1f63045390a"

    # find city, country
    g = geocoder.ip('me')
    location = geolocator.reverse(str(g.lat) + "," + str(g.lng)).raw['address']
    city = location.get('city')
    country = location.get('country')
    if city == 'Old Toronto':
        city = 'toronto'

    # request data openweather api
    url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
    res = requests.get(url)
    data = res.json()
    temp = round(data['main']['temp'])



    return (city, country, temp)

def get_time():
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M")
    return currentTime
    
if __name__ == "__main__":
    app.run(debug=True)