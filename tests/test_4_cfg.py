import numpy as np
from unittest import TestCase
import json

from src.datavis import from_cfg

sigma = 1  # 标准差
mean = 0  # 均值

np.random.seed(19680801)
x = mean + sigma * np.random.randn(10000)  # 正态分布随机数

with open("tests/test_4.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

file_name = "pic/test_4_直方图=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot, _ = from_cfg(cfg, x=x, bins=30)
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
