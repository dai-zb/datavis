from unittest import TestCase

import numpy as np

from src.datavis.config import PlotCfg, AxCfg, LegendCfg, FigCfg
from src.datavis import Plot
from src.datavis.style import Colors, Markers, LineStyles, Legends


def func():
    x = np.linspace(0, 5 * np.pi, 1000)
    y1 = np.sin(x)
    y2 = np.sin(2 * x)

    fig_cfg = FigCfg(
        columns_number=2
    )
    ax_cfg = AxCfg(title="fill between")
    plot = Plot(fig_cfg=fig_cfg, ax_cfg=ax_cfg)

    plot.plot(x, y1, label='y1')
    plot.plot(x, y2, label='y2')
    plot.fill_between(x, y1, y2, cfg=PlotCfg(color=Colors.green, alpha=0.3))

    legend_cfg = LegendCfg(location=Legends.upper_right, columns_number=1)
    plot.legend_set(cfg=legend_cfg)

    where1 = (y1 > y2).tolist()  # numpy to list
    plot.fill_between(x, y1, y2, where=where1, idx=1, label="a", cfg=PlotCfg(color=Colors.green, alpha=0.3))

    where2 = (y1 < y2).tolist()  # numpy to list
    plot.fill_between(x, y1, y2, where=where2, idx=1, label="b", cfg=PlotCfg(face_color=Colors.red, alpha=0.3))
    plot.legend_set(idx=1, cfg=legend_cfg)

    return plot


file_name = "pic/test_1b_fill_between=.png"


# class MyTestCase(TestCase):
#     def test_1(self):
#         plot = func()
#         plot.save(file_name)
#
#     # def test_2(self):
#     #     plot = func()
#     #     plot.save("test_1$.png")
#     #     plot.show()
