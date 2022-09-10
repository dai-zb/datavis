from unittest import TestCase

from src.datavis.config import PlotCfg, AxCfg
from src.datavis import Plot
from src.datavis.style import LineStyles
import numpy as np

np.random.seed(19680801)

# 画图区域大小
tang_data = [np.random.normal(0, std, 100) for std in range(6, 10)]


def func():
    ax_cfg = AxCfg(
        title="boxplot",
        x_label="x axis",
        y_label="y axis",
        grid=LineStyles.dotted,
    )
    plot = Plot(ax_cfg=ax_cfg)

    plot_cfg = PlotCfg(face_color='red', width=0.8)

    plot.box_plot(tang_data, vert=False, cfg=plot_cfg)

    return plot


file_name = "pic/test_5_箱线图=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot = func()
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
