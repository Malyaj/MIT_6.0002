#!/usr/bin/env python3

import numpy as np
import pandas as pd


class City(object):
    '''creating a polynomial object'''

    def __doc__():
        return '''This City class provides a way to represnt cities'''
    
    def __init__(self, name):
        self.name = name
        self.edges = dict()
    
    def __str__(self):
        name = self.name
        out = "City: " + name + " || "

        for k in self.edges.keys():
            out = out + ", " + k + " - " + str(self.edges[k])

        return out
        
    def __repr__(self):
        name = self.name
        return 'CIty: ' + name
    
    
    def addEdge(self, neighbour, distance):
        '''neighbour_kv is a tuple with the first element as neighbour city nane and the second as the distance'''
        self.edges[neighbour] = distance

    def getDistance(self, neighbour):
        if neighbour in self.edges.keys():
            return self.edges[neighbour]
        else:
            raise Exception


##dli = City('DLI')
##neighbours = [('KOL', 1500), ('BOM', 1420), ('JHS', 480), ('GZB', 40)]
##
##for each in neighbours:
##    dli.addEdge(each[0], each[1])
##
##for each in neighbours:
##    print(f"Distance of {each[0]} from Delhi is {dli.getDistance(each[0])}")
##
##print("-+-" * 30)

filepath = r"D:\Users\703143501\Desktop\cities.xlsx"
file = pd.ExcelFile(filepath)
df = file.parse('Sheet1')

cities = {}
cities_to = df.columns[1:]
cities_from = df['FROM']

for idx, city_from in enumerate(cities_from):

    ## create city from
    cities[city_from] = City(city_from)
    for city_to in cities_to:
        if not np.isnan(df[city_to][idx]):
            cities[city_from].addEdge(city_to, df[city_to][idx])


## distance of Bombay from Jhansi
#d = cities['JHS'].getDistance('BOM')
#print(d)

def distance(start, end):
    
    if start in cities and end in cities:
        try:
            return f"Distance of {end} from {start} is {cities[start].getDistance(end)}"
        except:
            print("No path exist between the cities")
            return None
    else:
        print("At least one of the cities is not part of the network!")
        return None

#print(distance('DLI', 'LKO'))

for city in cities:
    print(cities[city])

### next step would be to be able to navigate the graph
