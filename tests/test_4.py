import numpy as np
from unittest import TestCase

from src.datavis.config import FigCfg, PlotCfg
from src.datavis import Plot
from src.datavis.style import HistTypes, Colors

sigma = 1  # 标准差
mean = 0  # 均值

np.random.seed(19680801)
x = mean + sigma * np.random.randn(10000)  # 正态分布随机数


def func():
    fig_cfg = FigCfg(
        rows_number=2,
    )

    plot = Plot(fig_cfg=fig_cfg)

    cfg = PlotCfg(hist_type=HistTypes.step, face_color=Colors.yellow, alpha=0.75)
    plot.hist(x, bins=40, density=False, cumulative=False, cfg=cfg)
    cfg = PlotCfg(hist_type=HistTypes.bar, face_color=Colors.red, alpha=0.75, width=0.8)
    plot.hist(x, bins=20, density=True, cumulative=True, cfg=cfg, idx=1)
    return plot


file_name = "pic/test_4_直方图=.png"


# class MyTestCase(TestCase):
#     def test_1(self):
#         plot = func()
#         plot.save(file_name)
#
#     # def test_2(self):
#     #     plot = func()
#     #     plot.save(file_name)
#     #     plot.show()
