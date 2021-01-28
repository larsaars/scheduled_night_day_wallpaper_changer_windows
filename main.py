import requests as req
import os
import random
from datetime import datetime
import pytz
import ctypes

# define utc
utc = pytz.UTC

# get public ip address
ip = req.get('https://api.ipify.org').text
# request lat / lng
jsonLatLng = req.get('http://ip-api.com/json/' + ip).json()
# extract lat / lng
lat, lng = jsonLatLng['lat'], jsonLatLng['lon']
# request sunrise and sunset as json
ssJson = req.get('https://api.sunrise-sunset.org/json', params={'lat': lat, 'lng': lng}).json()['results']
# extract sunrise and sundown (in utc)
sunrise, sunset = ssJson['sunrise'], ssJson['sunset']

# current time (localize call necessary because python thinks this time is unaware)
now = utc.localize(datetime.now())


# extract datetime from string
def to_datetime(time):
    return utc.localize(datetime.strptime(time, '%I:%M:%S %p').replace(year=now.year, day=now.day, month=now.month))


# determine if is bright
day_start, day_end = to_datetime(sunrise), to_datetime(sunset)
is_bright = day_start <= now <= day_end

# if is dark, set night wallpaper, else one of day wallpapers
# determine absolute image path
dir_name = 'day' if is_bright else 'night'
path = os.path.abspath(dir_name + '/' + random.choice(os.listdir(dir_name)))
# set background (windows)
# if you are on another platform change the code here for it to work
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
