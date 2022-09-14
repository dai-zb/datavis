from unittest import TestCase
import os

from matplotlib import pyplot as plt

from src.datavis.config import FigCfg, PlotCfg, AxCfg
from src.datavis import Plot
from src.datavis.style import ColorMaps, Colors

pic_path = 'pic$.jpg'


def func():
    if os.path.exists(pic_path):
        img = plt.imread(pic_path)
    else:
        img = plt.imread(f"tests/{pic_path}")
    img1 = img[:, :, 0]

    fig_cfg = FigCfg(
        rows_number=2,
        columns_number=2,
        w_space=0,
        h_space=0.1,
    )
    ax_cfg = AxCfg(
        visible=False
    )
    plot = Plot(fig_cfg=fig_cfg, ax_cfg=ax_cfg)

    plot.im_show(img, idx=0)
    plot.add_box(["xyxy", 50, 50, 530, 540], label="ABC")

    plot.im_show(img1, idx=1, cfg=PlotCfg(colormap=ColorMaps.gray, color_bar=True))
    plot.add_box(["xywh", 50, 50, 480, 490], idx=1, label="ABC",
                 cfg=PlotCfg(face_color=Colors.blue, color=Colors.white, line_width=2, font_size=12))

    plot.im_show(img1, idx=2, cfg=PlotCfg(colormap=ColorMaps.hot, color_bar=True))
    plot.add_box(["xywh", 50, 50, 480, 490], idx=2,
                 cfg=PlotCfg(face_color=Colors.blue, color=Colors.white, line_width=2))
    plot.ax_set(idx=2, cfg=AxCfg(visible=True))

    plot.im_show(img1, idx=3, cfg=PlotCfg(colormap=ColorMaps.gray_r, color_bar=True))
    plot.add_box(["center_wh", 290, 295, 480, 490], idx=3, label="xyz",
                 cfg=PlotCfg(face_color=Colors.red, color=Colors.white, line_width=2))

    return plot


file_name = "pic/test_7_图片显示_colorbar_b-box=.png"

# class MyTestCase(TestCase):
#     def test_1(self):
#         plot = func()
#         plot.save(file_name)
#
#     # def test_2(self):
#     #     plot = func()
#     #     plot.save(file_name)
#     #     plot.show()
