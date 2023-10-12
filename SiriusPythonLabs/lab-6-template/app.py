# Пишем код тут
from LorenzAttractor.LorenzDynamics import LorenzDynamics, Interval, Noise
from LorenzAttractor import Point
from LorenzAttractor import Simulator
from animation import plot_animation, plot_static
from json_generation import *

if __name__ == '__main__':
    data = parsing_json('sample.json')

    lorenz = LorenzDynamics(0.02, Interval(-8, 8), Noise(0.01, 0.01, 0.01), 10,
                                           2.667, 28, Point(0, 1, 1.05))
    sym = Simulator(lorenz)
    t, all_points = sym.run()
    for i in range(len(t)):
        print("{}. t = {}, Point x = {}, y = {}, z = {}".format(i, t[i], all_points[0][i], all_points[1][i], all_points[2][i]))

    plot_static(all_points)
    #plot_animation(all_points)
