# Python code to make heuristics

# Chosen Heuristic: Straight Line Path - found using Geopy library of Python

import csv
from geopy.geocoders import Nominatim
 
citiesList = []
with open('roaddistance.csv', mode ='r')as file:
   
    csvFile = csv.reader(file)

    i=0
    for lines in csvFile:
        if i>0:
            citiesList.append(lines[0])
        i+=1

# Getting the co-ordinates of each city
cityCordinates = {}
geolocator = Nominatim(user_agent="AI_Assignment_2")
for city in citiesList:
    location = geolocator.geocode(city)
    cityCordinates[city] = (location.latitude, location.longitude)

# for city in citiesList:
#     print(city, ":", cityCordinates[city])

# Finding the straight line distance between each pair of cities
from geopy.distance import geodesic

f = open("heuristicdistance.pl", "w")

for c1 in citiesList:
    for c2 in citiesList:
        if c1!=c2:
            res = geodesic(cityCordinates[c1], cityCordinates[c2]).km
            res = int(res)
            f.write("heuristicDistance(" + "'" + c1 + "'" + ", " + "'" + c2 + "'" + ", " + str(res) + ").\n")

for c in citiesList:
    res = 0
    f.write("heuristicDistance(" + "'" + c + "'" + ", " + "'" + c + "'" + ", " + str(res) + ").\n")


# r = geodesic(cityCordinates['Ahmedabad'], cityCordinates['Bangalore']).km
# r = int(r)
# print("heuristicDistance(" + 'Ahmedabad' + ", " + 'Bangalore' + ", " + str(r) + ").")
# f.write("heuristicDistance(" + "'Ahmedabad'" + ", " + "'Bangalore'" + ", " + str(r) + ").\n")

# print("heuristicDistance(" + 'Ahmed' + ", " + 'Bang' + ", " + str(r) + ").")
# f.write("heuristicDistance(" + "'Ahmed'" + ", " + "'Bang'" + ", " + str(r) + ").\n")


f.close()

    
# print(citiesList)
# print()
# print(len(citiesList))