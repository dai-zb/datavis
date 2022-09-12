from unittest import TestCase

import numpy as np

from src.datavis import from_cfg

sigma = 1  # 标准差
mean = 0  # 均值
np.random.seed(19680801)
x = mean + sigma * np.random.randn(10000)  # 正态分布随机数

cfg = {
    "fig_cfg": {
        "figure_size": (5, 8),
        "rows_number": 3,
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
            "method": "violin_plot",
            "data": ["{{x}}"],
            "label": "abc",
            "idx": 1,
            "plot_cfg": {
                "width": 0.5,
                "face_color": 'red',
                "alpha": 0.2,
                "color": "Green",
            }
        },
        {
            "method": "violin_plot",
            "data": ["{{x}}"],
            "label": "abc",
            "idx": 2,
            "plot_cfg": {
                "width": 0.5,
                "face_color": 'red',
                "alpha": 0.5,
                "color": "Green",
            }
        },
        {
            "method": "box_plot",
            "data": ["{{x}}"],
            "idx": 2,
            "plot_cfg": {
                "width": 0.5
            }
        },
    ]
}

file_name = "pic/test_6a_直方图(hist)_小提琴图(violin_plot)=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot, _ = from_cfg(cfg, x=x, bins=40)
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
