from unittest import TestCase

from src.datavis.config import FigCfg, PlotCfg, AxCfg
from src.datavis import Plot
from src.datavis.style import LineStyles

x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = [23, 34, 53, 24, 34, 33, 21, 23, 41]
x2 = [3, 4, 5, 6, 7]
y2 = [2, 4, 3, 2, 7]


def func():
    fig_cfg = FigCfg(
        rows_number=2,
        columns_number=2,
        share_x_axis=True,
        share_y_axis=True,
    )

    plot = Plot(fig_cfg=fig_cfg)

    plot.plot(x1, y1)
    plot_cfg = PlotCfg(color='orange')
    plot.plot(x2, y2, idx=2, cfg=plot_cfg)

    plot.plot(x1, y1, idx=1)

    plot(x2, y2, idx=3, cfg=plot_cfg)
    ax_cfg = AxCfg(
        title="1",
        grid=LineStyles.dotted,
    )
    plot.ax_set(1, ax_cfg)

    return plot


file_name = "pic/test_3_多个子图_轴共享=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot = func()
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
