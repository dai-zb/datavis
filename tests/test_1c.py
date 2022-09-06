from unittest import TestCase

import numpy as np

from src.datavis.config import PlotCfg, AxCfg, LegendCfg, FigCfg
from src.datavis import Plot
from src.datavis.style import Colors, Markers, LineStyles, Legends


def func():
    x = np.linspace(0, 5 * np.pi, 8)
    y = np.sin(x)
    x_err = np.random.random(x.shape)
    y_err = np.random.random(y.shape) * 0.3

    fig_cfg = FigCfg(
        columns_number=3,
        figure_size=(12, 6)
    )
    ax_cfg = AxCfg(title="error_bar")
    plot = Plot(fig_cfg=fig_cfg, ax_cfg=ax_cfg)

    plot.error_bar(x, y, x_err, y_err, label='y', cfg=PlotCfg(face_color=Colors.red, width=5))
    legend_cfg = LegendCfg(location=Legends.upper_right, columns_number=1)
    plot.legend_set(cfg=legend_cfg)

    plot.error_bar(x, y, 1, 0.3, idx=1, label='z', cfg=PlotCfg(color=Colors.green,
                                                               marker=Markers.circle,
                                                               face_color=Colors.yellow, width=5))
    plot.ax_set(1, cfg=AxCfg(
        x_limit_left=-10,
        # x_limit_right=20,
        y_limit_bottom=-1.5,
        y_limit_top=1.5
    ))
    legend_cfg = LegendCfg(location=Legends.upper_right, columns_number=1)
    plot.legend_set(idx=1, cfg=legend_cfg)

    plot.error_bar(x, y, 1, 0.3, idx=2, label='z', cfg=PlotCfg(color=Colors.green,
                                                               line_width=3,
                                                               marker=Markers.circle,
                                                               face_color=Colors.yellow,
                                                               width=5))
    plot.ax_set(2, cfg=AxCfg(
        x_limit_left=-10,
        # x_limit_right=20,
        x_ticks=[-10, -5, 0, 5, 10, 15],
        x_tick_labels=["AAAAA", "BBBBB", "CCCCC", "DDDDD", "EEEEE", "FFFFF"],
        x_tick_rotation=30,

        y_limit_bottom=-1.5,
        y_limit_top=1.5,
        y_ticks=[-1.3, -0.2, 0.2, 1.3],
        y_tick_labels=["xxx", "yyy", "zzz", "aaa"],
        y_tick_rotation=30,

        tick_font_size=14,
    ))
    legend_cfg = LegendCfg(location=Legends.upper_right, columns_number=1)
    plot.legend_set(idx=2, cfg=legend_cfg)

    return plot


file_name = "pic/test_1c_error_bar_坐标范围=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot = func()
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save("test_1$.png")
    #     plot.show()
