from unittest import TestCase
import os

from matplotlib import pyplot as plt

from src.datavis.config import FigCfg, PlotCfg, AxCfg
from src.datavis import Plot
from src.datavis.style import Colors

pic_path = 'pic$.jpg'


def func():
    if os.path.exists(pic_path):
        img = plt.imread(pic_path)
    else:
        img = plt.imread(f"tests/{pic_path}")

    fig_cfg = FigCfg(
    )
    ax_cfg = AxCfg(
        # visible=False
    )
    plot = Plot(fig_cfg=fig_cfg, ax_cfg=ax_cfg)

    plot.im_show(img, cfg=PlotCfg(alpha=0.5))
    plot.mask([(100, 600), (200, 420), (250, 420), (450, 750), (550, 850), (650, 1100), (200, 1200), (100, 800)],
              label="abc",
              cfg=PlotCfg(
                  alpha=0.5, face_color=Colors.magenta,
                  font_size=20, color=Colors.white
              ))

    return plot


file_name = "pic/test_10_图片显示_mask=.png"


# file_name = "test_10_图片显示_mask=.png"


class MyTestCase(TestCase):
    def test_1(self):
        plot = func()
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
