from unittest import TestCase
from src.datavis import from_cfg
# from src.datavis.config import PlotCfg

import numpy as np

np.random.seed(19680801)

x = np.arange(-2, 5, 0.05)
y = 0.5 * x ** 2 + np.random.random(len(x)) * (x - 1.5) * 4

cfg = {
    "args": ["x", "y", "c"],
    "fig_cfg": {
        "columns_number": 2,
        "figure_size": (8, 4),
        "tight_layout": True,
    },
    "backend": "matplotlib",
    "plots": [
        {
            "method": "reg_plot",
            "data": {"x": "{{x}}", "y": "{{y}}", "c": "{{c}}"},
            "plot_cfg": {
                "color": "red",
                "line_width": 3,
            }
        },
        {
            "method": "reg_plot",
            "data": {"x": "{{x}}", "y": "{{y}}", "c": "{{c}}", "order": 3},
            "idx": 1,
            "plot_cfg": {
                "color": "blue",
                "line_width": 3,
            }
        },
    ]
}

file_name = "pic/test_13_reg_plot=.png"
# file_name = "test_13_reg_plot=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot, rets = from_cfg(cfg, x, y, "green")
        print(rets)
        # [[-2.4505598281617753, 3.643928664796404], [-3.1169877628133635, 2.4183293994354567, 0.3428164423853748, 0.015443266094270502]]
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
