# Created by Hannah at 06.10.2023 10:05
from Dot import Dot


class Building(Dot):

    def __init__(self, x, y, w):
        super().__init__(x, y)
        try:
            self.x = int(x)
            self.y = int(y)
        except TypeError:
            print("So sorry, but building used to have integer coordinates")
        try:
            self.w = float(w)
        except TypeError:
            print("So sorry, but point used to have numeric weight")

    def print_it(self):
        print("x = {}, y = {}, w = {}".format(self.x, self.y, self.w))

    def plus_w(self, w):
        self.w += w
        return self
