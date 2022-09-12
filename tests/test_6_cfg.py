from unittest import TestCase

import numpy as np

from src.datavis import from_cfg

sigma = 1  # 标准差
mean = 0  # 均值
np.random.seed(19680801)
x = mean + sigma * np.random.randn(10000)  # 正态分布随机数

cfg = {
    "fig_cfg": {
        "figure_size": (4, 6),
        "rows_number": 2,
        "share_x_axis": True,
    },
    "backend": "matplotlib",
    "plots": [
        {
            "method": "hist",
            "data": ["{{x}}", "{{bins}}"],
            "plot_cfg": {
                "hist_type": "step",
                "color": "Green",
            }
        },
        {
            "method": "box_plot",
            "data": ["{{x}}"],
            "idx": 1,
            "plot_cfg": {
                "width": 0.5
            }
        },
    ]
}

file_name = "pic/test_6_直方图(hist)_箱线图(boxplot)=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot, _ = from_cfg(cfg, x=x, bins=40)
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
