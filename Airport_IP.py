import requests


"""
https://github.com/ip2location/ip2location-iata-icao/blob/master/iata-icao.csv#L8970
"""

import csv
airport_list = []
with open('iata-icao.csv', 'r') as file:
  reader = csv.reader(file)
  # skip the 1st line of the file which is the header
  next(reader)
  for row in reader:
   airport_list.append( (row[2], row[-2],row[-1])  )

from math import radians, sin, cos, sqrt, atan2
def haversine(lat1, lon1, lat2, lon2):
  # Convert degrees to radians
  lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

  # Radius of the Earth in kilometers
  earth_radius = 6371

  # Haversine formula
  dlat = lat2 - lat1
  dlon = lon2 - lon1
  a = sin(dlat/2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon/2) ** 2
  c = 2 * atan2(sqrt(a), sqrt(1-a))
  distance = earth_radius * c
  return distance

# airport code --> weather
def airport_code_to_weather(airport_code):
  x = requests.get('http://wttr.in/'+airport_code+'?format="%C+%f"')
  return x.text

def ip_to_lat_lon(ip_address):
  response = requests.get(f'http://ip-api.com/json/{ip_address}')
  data = response.json()
  return (data['lat'],data['lon'])

def location_to_nearest_airport_code(location):
  distances_and_names=[]
  for name, lat, lon in airport_list:
    distance = haversine(location[0], location[1], float(lat), float(lon))
    distances_and_names.append(  [distance,name] )
  # Find the smallest distancesdistance
  smallest_distance = min(distances_and_names)
  print(smallest_distance)
  return smallest_distance[1]

ip_address = "104.75.97.17"
location = ip_to_lat_lon(ip_address)
print(location)
airport_code = location_to_nearest_airport_code(location)
weather = airport_code_to_weather(airport_code)
print(weather)