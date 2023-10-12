# Created by Hannah at 06.10.2023 9:53
from Dot import Dot
from Building import Building
import math


class RacketShot(Dot):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        try:
            self.r = float(r)
        except TypeError:
            print("So sorry, but point used to have numeric radius")
        self.w = 0

    def __lt__(self, other):
        if self.r >= other.r:
            return False
        return True

    def if_shot(self, other):
        if self.dot_dist_kv(other) <= self.r ** 2:
            return True
        return False

    def weight_of_shot(self, dot_arr):
        for i in range(math.ceil(self.x - self.r), math.ceil(self.x + self.r)):
            for j in range(math.floor(self.y - self.r), math.ceil(self.y + self.r) + 1):
                if 0 <= i < len(dot_arr) and 0 <= j < len(dot_arr):
                    b = Building(i, j, dot_arr[i][j])
                    if self.if_shot(b):
                        self.w += b.w
                    else:
                        break
        return self.w
