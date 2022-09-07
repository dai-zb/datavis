from unittest import TestCase

import numpy as np

from src.datavis.config import PlotCfg, AxCfg, FigCfg
from src.datavis import Plot
from src.datavis.style import LineStyles, ColorMaps


def func():
    np.random.seed(19680801)

    n = 5000
    # 产生均值为0标准差为1区间的n个服从正态分布的随机数
    x = np.random.normal(0, 1, n)
    y = np.random.normal(0, 1, n)

    # 获取颜色的分布对应值
    c_color = np.sqrt(x ** 2 + y ** 2)

    fig_cfg = FigCfg(
        columns_number=2,
        figure_size=(10, 4),
    )

    ax_cfg = AxCfg(
        title="Scatter",
        title_font_size=20,

        x_label="x",
        y_label="y",
        label_font_size=12,
        grid=LineStyles.dotted,
    )

    plot = Plot(fig_cfg=fig_cfg, ax_cfg=ax_cfg)

    cfg = PlotCfg(colormap=ColorMaps.jet_r, alpha=0.5, color_bar=True)

    plot.scatter(x, y, s=60, c=c_color, cfg=cfg)

    np.random.seed(19680801)

    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii

    plot.scatter(x, y, s=area, c=colors, idx=1, cfg=PlotCfg(alpha=0.5, color_bar=True))
    plot.ax_set(1, AxCfg(title="bubble"))

    return plot


file_name = "pic/test_2_散点图_气泡图_字体尺寸=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot = func()
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
