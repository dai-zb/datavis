from unittest import TestCase

import numpy as np

from src.datavis.config import PlotCfg, AxCfg, LegendCfg
from src.datavis import Plot
from src.datavis.style import Colors, Markers, LineStyles, Legends


def func():
    x = np.linspace(-np.pi, np.pi, 25)
    # -PI 到 PI，间隔为256的等差序列
    # 点要足够多，否则不光滑
    y = np.sin(x)
    z = np.cos(x)
    u = np.cos(x) + 2
    v = np.cos(2 * x) + 4

    ax_cfg = AxCfg(title="line style", x_label="x axis", y_label="yy yy yy")

    plot = Plot(ax_cfg=ax_cfg)

    plot.plot(x, y, label='legend-xy', cfg=PlotCfg(color=Colors.blue))

    plot_cfg = PlotCfg(
        color=Colors.green,
        marker=Markers.circle,
        line_style=LineStyles.dashed,
        line_width=2,
        marker_size=12
    )
    plot.plot(x, z, label='legend-xz', cfg=plot_cfg)
    plot.plot(x, u, label='legend-xu', cfg=plot_cfg.set_value("color", Colors.yellow))

    plot_cfg = PlotCfg(
        color=Colors.red,
        marker=Markers.plus,
        line_style=LineStyles.dashed
    )
    plot.plot(x, v, label='legend-xv', cfg=plot_cfg)

    legend_cfg = LegendCfg(location=Legends.upper_right, columns_number=1)
    plot.legend_set(cfg=legend_cfg)

    return plot


file_name = "pic/test_1_折线图=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot = func()
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save("test_1$.png")
    #     plot.show()
