import tkinter
from tkinter import ALL


def create_map(window, offset_x, offset_y, cities, city_size):
    for i in range(len(cities)):
        cities[i][0] = cities[i][0] * 2 + offset_x
        cities[i][1] = cities[i][1] * 2 + offset_y

    cities.append(cities[0])
    window.create_line(cities)

    for city in cities:
        x = city[0]
        y = city[1]

        window.create_oval(x - city_size / 2, y - city_size / 2, x + city_size / 2, y + city_size / 2, fill="Red")


def gui(window, cities):
    window.update()
    window.delete(ALL)

    create_map(window, 50, 50,  cities, 6 * 2)
