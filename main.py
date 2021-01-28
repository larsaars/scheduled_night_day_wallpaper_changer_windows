import requests as req
import os
import random
from datetime import datetime
import pytz
import ctypes

# define utc
utc = pytz.UTC

# inform user what is happening
os.system('title wallpaper swap')

# get public ip address
print('getting public ip')
ip = req.get('https://api.ipify.org').text

# request lat / lng
print('extracting latitude and longitude from ip')
json_lat_lng = req.get('http://ip-api.com/json/' + ip).json()
# extract lat / lng
lat, lng = json_lat_lng['lat'], json_lat_lng['lon']

# request sunrise and sunset as json
print('requesting sunrise and sunset time')
json_ss = req.get('https://api.sunrise-sunset.org/json', params={'lat': lat, 'lng': lng}).json()['results']
# extract sunrise and sundown (in utc)
sunrise, sunset = json_ss['sunrise'], json_ss['sunset']

# current time (localize call necessary because python thinks this time is unaware)
now = utc.localize(datetime.now())


# extract datetime from string
def to_datetime(time):
    return utc.localize(datetime.strptime(time, '%I:%M:%S %p').replace(year=now.year, day=now.day, month=now.month))


# determine if is bright
day_start, day_end = to_datetime(sunrise), to_datetime(sunset)
is_bright = day_start <= now <= day_end

# if is dark, set night wallpaper, else one of day wallpapers
print('setting random wallpaper, is_bright = %r' % is_bright)
# determine absolute image path
dir_name = 'day' if is_bright else 'night'
path = os.path.abspath(dir_name + '/' + random.choice(os.listdir(dir_name)))
# set background (windows)
# if you are on another platform change the code here for it to work
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
