from unittest import TestCase

import numpy as np

from src.datavis import from_cfg

data_dict = {
    "first": [20, 34, 30, 35, 27],
    "second": [25, 32, 34, 20, 25],
    "third": [21, 31, 37, 21, 28],
    "fourth": [26, 31, 35, 27, 21],
}

_data = list(data_dict.values())
_data = np.array(_data)
data = _data.T

x = list(range(5))

cfg = {
    "fig_cfg": {
        "columns_number": 2,
    },
    "backend": "matplotlib",
    "plots": [
        {
            "method": "plot",
            "data": [x, data],
            "label": list(data_dict.keys()),
            "legend_cfg": {}
        },
        {
            "method": "stack_plot",
            "data": [x, _data],
            "idx": 1,
            "label": list(data_dict.keys()),
            "legend_cfg": {}
        },
    ]
}

file_name = "pic/test_1a_折线图_面积堆叠图=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot, _ = from_cfg(cfg)
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
