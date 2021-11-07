from simulated_annealing import *
from evolution import *
from tabu import *

answer = input("SIZE [X Y]: ")
size = answer.split(" ")
size[0] = int(size[0])
size[1] = int(size[1])
window = tkinter.Canvas(width=50 * 2 + size[0] * 2, height=50 * 2 + size[1] * 2)

number = int(input("Number of cities:"))
cities = gen_cities(size, number)

window.pack()

algorithm = input("Simulated annealing[1] | Evolution algorithm[2] | Tabu search[3] \n")

max = int(input("Max neighbour distance: "))

gui_toggle = int(input("Show searching progress?[0/1] "))

if algorithm == "1":
    t = 50
    cooling = input("Cooling rate [0-5]: ")
    if cooling == "5":
        Z = 0.99
    elif cooling == "4":
        Z = 0.995
    elif cooling == "3":
        Z = 0.997
    elif cooling == "2":
        Z = 0.999
    elif cooling == "1":
        Z = 0.9995
    elif cooling == "0":
        Z = 0.9999
    else:
        Z = 0.995
    simulated_annealing(window, cities, t, Z, max-1, gui_toggle)

    window.mainloop()

elif algorithm == "2":
    evolution_algorithm(window, cities, len(cities), max-1, gui_toggle)

    window.mainloop()

elif algorithm == "3":
    list_size = input("Size of tabu memory: ")
    moves_threshold = input("Threshold: ")
    tabu_search(window, cities, int(list_size), int(moves_threshold), max-1, gui_toggle)

    window.mainloop()

else:
    exit(1)

