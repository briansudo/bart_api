#!/usr/bin/env python 

import requests
from xml.etree import ElementTree as ET

KEY = 'QMLH-JM5H-II2Q-DT35'

etd_url = 'http://api.bart.gov/api/etd.aspx'
cmd = 'etd'
orig = raw_input('Origin: ') or 'DBRK'
platform = None;
direction = None;
param = {'cmd': cmd, 'orig': orig, 'key': KEY, 'plat': platform, 'dir': direction}

r = requests.get(etd_url, params=param)
root = ET.fromstring(r.content)

date = root.find('date').text
time = root.find('time').text
origin = root.find('station').find('name').text
destination = root.find('station').find('etd').find('destination').text
next_trains = root.find('station').find('etd').findall('estimate')
next_train_mins = []
next_train_lens = []

for train in next_trains:
    next_train_mins += [train.find('minutes').text]
    next_train_lens += [train.find('length').text]

print("Today is " + date)
print("Request time is " + time)
print("Origin: " + origin)
print("Destination: " + destination)
print("The next trains will arrive at the station in " + ', '.join(next_train_mins[:-1]) + ", and " + next_train_mins[-1] + " minutes.")
print("The next trains have " + ', '.join(next_train_lens[:-1]) + ", and " + next_train_lens[-1] + " cars.")


