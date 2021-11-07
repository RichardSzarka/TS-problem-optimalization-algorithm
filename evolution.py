import time
from Classes import *
from city_manipulations import *
import operator
import sys
from copy import deepcopy
from GUI import *


def getaverage(gen):
    rating = 0
    for cities in gen:
        rating += cities.rating

    return rating//len(gen)


def duplicates(cities, base, X):
    duplicates = []
    missing = []
    for i in range(len(cities)):
        for j in range(len(cities)):
            if str(cities[i]) == str(cities[j]) and i != j:
                if cities[i] not in duplicates:
                    duplicates.append(cities[i])

    for i in base:
        if i not in cities:
            missing.append(i)

    if X % 2 == 0:
        for i in range(len(cities)-1, 0, -1):
            if len(missing) == 0:
                break
            if cities[i] in duplicates:
                cities[i] = missing[0]
                missing.pop(0)
    else:
        for i in range(len(cities)):
            if len(missing) == 0:
                break
            if cities[i] in duplicates:
                cities[i] = missing[0]
                missing.pop(0)

    return cities


def evolution_algorithm(window, cities, count, max, toggle):
    gen = []
    generation = 0
    base_cities = deepcopy(cities)

    for i in range(100):
        new_cities = deepcopy(cities)
        random.shuffle(new_cities)
        new_travel = Cities(new_cities, fitness(new_cities))
        gen.append(new_travel)

    gen = sorted(gen, key=operator.attrgetter("rating"))
    gen = gen[:10]

    if toggle == 1:
        gui(window, deepcopy(gen[0].cities))

    while True:
        generation += 1
        average = getaverage(gen)
        sys.stdout.write("\r" + "Average rating: " + str(average) + " | Best individual" + str(gen[0].rating) +
                     " | Generation: " + str(generation) )
        new_gen = []
        for i in range(10):
            for j in range(10):
                new_cities = gen[i].cities[:count//2] + gen[j].cities[count//2:]
                new_cities = duplicates(new_cities, base_cities, j)
                new_travel = Cities(new_cities, fitness(new_cities))
                new_gen.append(new_travel)

        gen = sorted(new_gen, key=operator.attrgetter("rating"))
        gen = gen[:10]

        for i in range(5, 10):
            gen[i].cities = find_neighbor(gen[i].cities, max)
            gen[i].rating = fitness(gen[i].cities)

        time.sleep(0.1)
        gui(window, deepcopy(gen[0].cities))


