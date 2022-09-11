from unittest import TestCase

import json

import numpy as np

from src.datavis import from_cfg

x = np.linspace(0, 5 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.sin(2 * x)

where1 = (y1 > y2).tolist()  # numpy to list
where2 = (y1 < y2).tolist()  # numpy to list

with open("tests/test_1b.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

file_name = "pic/test_1b_fill_between=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot, _ = from_cfg(cfg, x=x, y1=y1, y2=y2, where1=where1, where2=where2)
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save("test_1$.png")
    #     plot.show()
