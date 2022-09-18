from unittest import TestCase
from src.datavis import from_cfg

import numpy as np

np.random.seed(19680801)
mat = np.random.random([7, 7])

cfg = {
    "args": ["x", "y", "x1", "c"],
    "fig_cfg": {
        "columns_number": 2,
        "figure_size": (8, 4),
        "tight_layout": True,
    },
    "backend": "matplotlib",
    "plots": [
        {
            "method": "q_q_plot",
            "data": ["{{x}}", "{{y}}"],
        },
        {
            "method": "q_q_plot",
            "data": {"data": "{{x1}}", "c": "{{c}}"},
            "idx": 1,
            "plot_cfg": {
                "color": "red",
            }
        },
    ]
}

file_name = "pic/test_12_q_q_plot=.png"
# file_name = "test_12_q_q_plot=.png"

x = np.array([9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7])
y = np.array([23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61])

data = np.random.normal(size=1000) ** 2 + \
       10 * np.random.normal(loc=100, scale=10, size=1000) * \
       np.random.normal(loc=100, scale=15, size=1000)  # 产生随机数据


class MyTestCase(TestCase):
    def test_1(self):
        plot, rets = from_cfg(cfg, x, y, data, c="green")
        print(rets)
        # [(0.647456422533105, -1.2874205132042107), (18365.11580916711, 100012.67456060456)]
        # plot.backend.fig.tight_layout()
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
