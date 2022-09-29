from unittest import TestCase

import numpy as np

from src.datavis.config import LegendCfg, FigCfg
from src.datavis import Plot


def func():
    data_dict = {
        "first": [20, 34, 30, 35, 27],
        "second": [25, 32, 34, 20, 25],
        "third": [21, 31, 37, 21, 28],
        "fourth": [26, 31, 35, 27, 21],
    }

    _data = list(data_dict.values())
    _data = np.array(_data)
    data = _data.T
    print(data.shape)  # (5, 4)

    x = list(range(5))

    fig_cfg = FigCfg(columns_number=2)

    plot = Plot(fig_cfg=fig_cfg)

    plot.plot(x, data, label=list(data_dict.keys()))  # 输入的尺寸是不同的
    # plot.stackplot(x, data_dict.values(), label=list(data_dict.keys()), idx=1)
    plot.stack_plot(x, _data, label=list(data_dict.keys()), idx=1)

    plot.legend_set(0, LegendCfg())
    plot.legend_set(1, LegendCfg())

    return plot


file_name = "pic/test_1a_折线图_面积堆叠图=.png"


# class MyTestCase(TestCase):
#     def test_1(self):
#         plot = func()
#         plot.save(file_name)
#
#     # def test_2(self):
#     #     plot = func()
#     #     plot.save(file_name)
#     #     plot.show()
