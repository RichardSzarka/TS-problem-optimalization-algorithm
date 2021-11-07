from city_manipulations import *
from GUI import *
from copy import deepcopy
from math import exp
import sys


def simulated_annealing(window, cities, t, Z, max, toggle):
    best_cities = cities
    best_rating = fitness(cities)
    rating = fitness(cities)
    iteration = 0
    worse = 0
    while True:
        sys.stdout.write("\r" + "Temperature:" + str(t) + " | best: " + str(best_rating) +
            "| worse accepted:" + str(worse))  # výpis
        if iteration % 10:
            t = t * Z
        if toggle == 1:
            gui(window, deepcopy(cities))

        new_cities = find_neighbor(deepcopy(cities), max)
        new_rating = fitness(new_cities)

        diff = rating - new_rating
        if diff > 0:
            cities = new_cities
            rating = new_rating
            if best_rating > new_rating:
                best_cities = new_cities
                best_rating = new_rating
        else:
            if exp(diff / t) >= random.random():
                if rating < new_rating:
                    worse += 1
                cities = new_cities
                rating = new_rating

        iteration += 1

        if t < 0.03:
            break

    gui(window, best_cities)
