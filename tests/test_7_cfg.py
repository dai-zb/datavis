from unittest import TestCase
import os
import json

from matplotlib import pyplot as plt

from src.datavis import from_cfg

pic_path = 'pic$.jpg'
if os.path.exists(pic_path):
    img = plt.imread(pic_path)
else:
    img = plt.imread(f"tests/{pic_path}")
img1 = img[:, :, 0]

box = ["xyxy", 50, 50, 530, 540]
box1 = ["xywh", 50, 50, 480, 490]
box3 = ["center_wh", 290, 295, 480, 490]

with open("tests/test_7.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

file_name = "pic/test_7_图片显示_colorbar_b-box=.png"


# file_name = "test_7_图片显示_colorbar_b-box=.png"


class MyTestCase(TestCase):
    def test_1(self):
        # plot = from_cfg(cfg, img=img, box=box, img1=img1, box1=box1, box3=box3)
        plot, _ = from_cfg(cfg, img=img, img1=img1, box=box, box1=box1, box3=box3)
        plot.save(file_name)

    # def test_2(self):
    #     plot = func()
    #     plot.save(file_name)
    #     plot.show()
