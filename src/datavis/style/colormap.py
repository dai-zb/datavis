from .info import Info
from .base import BaseEnum


class ColorMaps(BaseEnum):
    jet = Info("jet", matplotlib="jet")
    jet_r = Info("jet_r", matplotlib="jet_r")
    gray = Info("gray", matplotlib="gray")
    gray_r = Info("gray_r", matplotlib="gray_r")
    hot = Info("hot", matplotlib="hot")
    hot_r = Info("hot_r", matplotlib="hot_r")
    OrRd = Info("OrRd", matplotlib="OrRd")
    rainbow = Info("rainbow", matplotlib="rainbow")
    binary = Info("binary", matplotlib="binary")


