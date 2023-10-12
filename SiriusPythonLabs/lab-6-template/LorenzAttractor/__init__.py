# Created by Hannah at 10.10.2023 15:16

import math
from dataclasses import dataclass

import numpy as np
from scipy import integrate


@dataclass
class Point:
    x: float
    y: float
    z: float

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)


class Simulator:

    def __init__(self, dynamicFunc):
        self.dynamicFunc = dynamicFunc

    def run(self):
        interval = self.dynamicFunc.interval
        step = self.dynamicFunc.step
        start_xyz = self.dynamicFunc.start_xyz

        t = []
        dt = interval.t0
        while dt < interval.t1:
            t.append(dt)
            dt += step

        # это можно сделать так вместо массива t, но там кривой шаг будет
        t = np.linspace(interval.t0, interval.t1, int((interval.t1 - interval.t0) // step))

        all_xyz = integrate.solve_ivp(self.dynamicFunc.__call__, (interval.t0, interval.t1), [start_xyz.x, start_xyz.y, start_xyz.z], t_eval=t)
        all_xyz = np.array(all_xyz.y)

        return t, all_xyz
