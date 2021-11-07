import random
import math


def gen_cities(size, number):
    i = 0
    cities = []

    while i < number:
        found = False
        x = random.randint(0, size[0])
        y = random.randint(0, size[1])

        for city in cities:
            if abs(city[0] - x) < 8 and abs(city[1] - y) < 8:
                found = True

        if found:
            continue

        city = [x, y]
        cities.append(city)

        i += 1

    return cities


def find_neighbor(cities, max):
    r = random.randint(0, max)

    city1 = random.randint(0, len(cities) - 1)
    city2 = random.randint(0, len(cities) - 1)

    while city1 == city2:
        city1 = random.randint(0, len(cities) - 1)
        city2 = random.randint(0, len(cities) - 1)

    help = cities[city1]
    cities[city1] = cities[city2]
    cities[city2] = help

    for i in range(r):
        city1 = random.randint(0, len(cities) - 1)
        city2 = random.randint(0, len(cities) - 1)

        while city1 == city2:
            city1 = random.randint(0, len(cities) - 1)
            city2 = random.randint(0, len(cities) - 1)

        help = cities[city1]
        cities[city1] = cities[city2]
        cities[city2] = help

    return cities


def fitness(cities):
    rating = 0
    for i in range(len(cities) - 1):
        x = abs(cities[i][0] - cities[i + 1][0])
        y = abs(cities[i][1] - cities[i + 1][1])
        size = x * x + y * y
        rating += math.sqrt(size)

    x = abs(cities[0][0] - cities[-1][0])
    y = abs(cities[0][1] - cities[-1][1])
    rating += math.sqrt(x * x + y * y)

    return rating
