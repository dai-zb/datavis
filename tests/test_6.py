from unittest import TestCase

import numpy as np

from src.datavis.config import FigCfg, PlotCfg
from src.datavis import Plot
from src.datavis.style import HistTypes, Colors

sigma = 1  # 标准差
mean = 0  # 均值
np.random.seed(19680801)
x = mean + sigma * np.random.randn(10000)  # 正态分布随机数


def func():
    fig_cfg = FigCfg(
        figure_size=(4, 6),
        rows_number=2,
        share_x_axis=True,

    )
    plot = Plot(fig_cfg=fig_cfg)
    plot.hist(x, bins=40, idx=0, cfg=PlotCfg(hist_type=HistTypes.step, color=Colors.green))

    plot.boxplot(x, label="box", idx=1, cfg=PlotCfg(width=0.5))

    return plot


file_name = "pic/test_6_直方图(hist)_箱线图(boxplot)=.png"


# class MyTestCase(TestCase):
#     def test_1(self):
#         plot = func()
#         plot.save(file_name)
#
#     # def test_2(self):
#     #     plot = func()
#     #     plot.save(file_name)
#     #     plot.show()
