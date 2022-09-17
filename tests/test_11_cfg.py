from unittest import TestCase
from src.datavis import from_cfg

import numpy as np

np.random.seed(19680801)
mat = np.random.random([7, 7])

cfg = {
    "args": ["mat"],
    "fig_cfg": {
        "columns_number": 2,
        "figure_size": (8, 4),
    },
    "backend": "matplotlib",
    "plots": [
        {
            "method": "mat_show",
            "data": ["{{mat}}"],
            "plot_cfg": {
                "colormap": "OrRd",
                "color_bar": True,
                "font_size": 12,
                "fmt": "%.1f"
            }
        },
        {
            "method": "mat_show",
            "data": ["{{mat}}"],
            "idx": 1,
            "plot_cfg": {
                "colormap": "hot_r",
                "color_bar": True,
                "font_size": 8,
                "fmt": "%.2f"
            }
        },
    ]
}

file_name = "pic/test_11_matshow=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot, _ = from_cfg(cfg, mat)
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
