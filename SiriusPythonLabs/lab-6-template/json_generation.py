# Created by Hannah at 12.10.2023 13:32
import dataclasses
import json
from dataclasses import dataclass

from LorenzAttractor.LorenzDynamics import Interval, Noise
from LorenzAttractor import Point


@dataclass
class InputData:
    step: float
    interval: Interval
    noise: Noise
    sigma: float
    beta: float
    ro: float
    start_point: Point

    @classmethod
    def from_dict(cls, data):
        return cls(
            step=data.get('step'),
            interval=Interval(data.get('interval').get('t0'), data.get('interval').get('t1')),
            noise=Noise(data.get('noise').get('sig_x'), data.get('noise').get('sig_y'), data.get('noise').get('sig_z')),
            sigma=data.get('sigma'),
            beta=data.get('beta'),
            ro=data.get('ro'),
            start_point=Point(data.get('start_point').get('x'), data.get('start_point').get('y'), data.get('start_point').get('z'))
        )


def create_json():
    id = InputData(0.02, Interval(0, 75), Noise(0.01345, 0.01, 0.01), 10, 2.667, 28, Point(0, 1, 1.05))

    json_object = json.dumps(dataclasses.asdict(id))

    with open("sample.json", "w") as outfile:
        outfile.write(json_object)


def parsing_json(path):
    with open(path, 'r') as openfile:
        json_object = json.load(openfile)
    id = InputData.from_dict(json_object)
    print(id)
    print(type(id))
    return id


if __name__ == '__main__':
    parsing_json()
