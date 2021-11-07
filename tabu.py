import time

from city_manipulations import *
from GUI import *
from copy import deepcopy
from Classes import *
import sys
import operator


def hash(cities):
    string = ""
    for city in cities.cities:
        string += str(city)

    return string


def tabu_search(window, cities_list, list_size, threshold, max, toggle):
    tabu_list = []
    iteration = 0
    best_city = Cities(cities_list, fitness(cities_list))
    cities = Cities(cities_list, fitness(cities_list))
    while True:
        sys.stdout.write("\r"+"Iteration: "+str(iteration))
        cities_array = []
        if toggle == 1:
            gui(window, deepcopy(cities.cities))

        for i in range(50):
            new_cities = find_neighbor(deepcopy(cities.cities), max)
            new = Cities(new_cities, fitness(new_cities))
            cities_array.append(new)

        cities_array = sorted(cities_array, key=operator.attrgetter("rating"))

        found = False
        for city in cities_array:
            if hash(city) in tabu_list:
                continue
            found = True
            cities = city
            break

        if not found:
            continue

        if cities.rating < best_city.rating:
            best_city = cities

        tabu_list.append(hash(cities))

        if len(tabu_list) > list_size:
            tabu_list.pop(0)

        iteration += 1

        if iteration > threshold:
            break

    gui(window, deepcopy(best_city.cities))

