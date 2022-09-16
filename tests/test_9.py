from unittest import TestCase

from src.datavis.config import LegendCfg, FigCfg, PlotCfg
from src.datavis import Plot


def func():
    x = ['C0', 'C1', 'C2', 'C3', 'C4']
    data = [20, 34, 30, 35, 27]
    data1 = [34, 30, 35, 27, 18]

    fig_cfg = FigCfg(columns_number=2)

    plot = Plot(fig_cfg=fig_cfg)

    plot.bar(x, data, label="1",
             cfg=PlotCfg(color=x))
    plot.bar(x, data, label="1", idx=1)
    plot.bar(x, data1, bottom=data, label="2", idx=1)

    # plot.legend_set(0, LegendCfg())
    plot.legend_set(1, LegendCfg())

    return plot


file_name = "pic/test_9_柱状图_堆叠=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot = func()
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
