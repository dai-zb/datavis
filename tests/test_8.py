from unittest import TestCase

from src.datavis.style import Colors
from src.datavis.config import LegendCfg, FigCfg, PlotCfg
from src.datavis import Plot


def func():
    x = ['G1', 'G2', 'G3', 'G4', "G5"]
    data = [20, 34, 30, 35, 27]
    data1 = [34, 30, 35, 27, 18]

    fig_cfg = FigCfg(columns_number=2)

    plot = Plot(fig_cfg=fig_cfg)

    plot.bar(x, data, label="1")
    plot.pie(x, data1, label="2", idx=1, cfg=PlotCfg(
        color=[Colors.red, Colors.green, Colors.blue, Colors.yellow, Colors.magenta]
    ))

    plot.legend_set(0, LegendCfg())
    return plot


file_name = "pic/test_8_柱状图_饼图=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot = func()
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
