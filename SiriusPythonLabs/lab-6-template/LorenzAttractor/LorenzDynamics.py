# Created by Hannah at 10.10.2023 15:16

import numpy as np
from dataclasses import dataclass


@dataclass
class Interval:
    t0: int
    t1: int


@dataclass
class Noise:
    sig_x: float
    sig_y: float
    sig_z: float

    def __init__(self, sig_x, sig_y, sig_z):
        self.sig_x = sig_x
        self.sig_y = sig_y
        self.sig_z = sig_z
        self.sig_z_new = np.random.normal(0, self.sig_z)
        self.sig_y_new = np.random.normal(0, self.sig_y)
        self.sig_x_new = np.random.normal(0, self.sig_x)

    def regenerate(self):
        self.sig_z_new = np.random.normal(0, self.sig_z)
        self.sig_y_new = np.random.normal(0, self.sig_y)
        self.sig_x_new = np.random.normal(0, self.sig_x)
        return self.sig_x_new, self.sig_y_new, self.sig_z_new


class LorenzDynamics():
    def __init__(self, step, interval, noise, sigma, beta, ro, start_xyz):
        self.step = step
        self.interval = interval
        self.noise = noise
        self.sigma = sigma
        self.beta = beta
        self.ro = ro
        self.start_xyz = start_xyz

    def __call__(self, t, yk):
        self.noise.regenerate()
        x, y, z = yk
        # dxdt = [x[1], self.sigma * (y[0] - x[0]) + self.noise.sig_x_new]
        dxdt = self.sigma * (y - x) + self.noise.sig_x_new
        # dydt = [y[1], x[0] * (self.ro - z[0]) - y[0] + self.noise.sig_y_new]
        dydt = x * (self.ro - z) - y + self.noise.sig_y_new
        # dzdt = [z[1], x[0] * y[0] - self.beta * z[0] + self.noise.sig_z_new]
        dzdt = x * y - self.beta * z + self.noise.sig_z_new
        return [dxdt, dydt, dzdt]
