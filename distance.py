#OpenFlights data
import csv

latitudes = {}
longitudes = {}

file1 = open("airports.dat")
for row in csv.reader(file1):
    # if row[3]=="Poland":
    airport_id = row[0]
    latitudes[airport_id] = float(row[6])
    longitudes[airport_id] = float(row[7])

from math import cos,radians,sin,pow,asin,sqrt

def eucli_distance(latA, longA, latB, longB):
    e_radius = 6371  # promień Ziemi
    latA = radians(latA)
    longA = radians(longA)
    latB = radians(latB)
    longB = radians(longB)

    dist_lat = latA - latB
    dist_long = longA - longB

    # wyliczanie ortodromy
    dist = 2 * e_radius * asin(sqrt(pow(sin(dist_lat/2),2) + cos(latA)*cos(latB)*pow(sin(dist_long/2),2)))
    return dist

distances = []
file2 = open("routes.dat")
for row in csv.reader(file2):
    start_airport = row[3]
    end_airport = row[5]
    if start_airport in longitudes and end_airport in longitudes:
        start_lat = latitudes[start_airport]
        start_long = longitudes[start_airport]
        end_lat = latitudes[end_airport]
        end_long = longitudes[end_airport]
        distances.append(eucli_distance(start_lat, start_long, end_lat, end_long))

import numpy
import matplotlib.pyplot as plt

plt.hist(distances,50)
plt.title('Połączenia lotnicze')
plt.xlabel("Dystans w km")
plt.ylabel("Liczba lotów")
plt.show()

plt.hist(distances,50,range=(0,4000))
plt.title('Połączenia lotnicze do 4000km')
plt.xlabel("Dystans w km")
plt.ylabel("Liczba lotów")
plt.show()

long_dist = 100 * len([k for k in distances if k > 5000]) / len(distances)
medium_dist = 100 * len([k for k in distances if k <= 5000 and k >= 1000]) / len(distances)
short_dist = 100 * len([k for k in distances if k < 1000]) / len(distances)

objects = ('<1000', '1000-5000', '>5000')
x = numpy.arange(len(objects))
bars = [short_dist, medium_dist, long_dist]
 
plt.bar(x, bars, align='center')
plt.xticks(x, objects)
plt.xlabel("Dystans w km")
plt.ylabel('%')
plt.title('% Połączeń lotniczych')
 
plt.show()


