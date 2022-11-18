from typing import Tuple, Union, Optional

from .base import BaseEnum
from .info import Info


def hex_to_rgb(hex_value: str) -> Tuple[int, int, int]:
    if len(hex_value) == 6:
        r = hex_value[:2]
        g = hex_value[2:4]
        b = hex_value[4:]
        return int(r, 16), int(g, 16), int(b, 16)
    elif len(hex_value) == 3:
        r = hex_value[0]
        g = hex_value[1]
        b = hex_value[2]
        return int(r, 16), int(g, 16), int(b, 16)
    raise ValueError(f"{hex_value} can not convert to rgb")


def rgb_to_hex(red: Union[int, float], green: Union[int, float], blue: Union[int, float]) -> str:
    if 0 <= red <= 255 and 0 <= red <= 255 and 0 <= red <= 255:
        s = hex(int(red * 256 * 256 + green * 256 + blue))
        return s[2:].zfill(6)
    else:
        return ""
        # raise ValueError(f"{red},{green},{blue} can not convert to rgb")


class ColorInfo(Info):
    def __init__(self, name: str, cn_name, rgb: Tuple[int, int, int], **kwargs):
        super().__init__(name, **kwargs)
        self.name: str = name
        self.cn_name: Tuple[str, ...] = (cn_name,) if isinstance(cn_name, str) else cn_name
        self.hex_value: str = rgb_to_hex(*rgb)
        self.rgb: Tuple[int, int, int] = rgb

    def __getitem__(self, item):
        if item in self:
            return super().__getitem__(item)
        return self.name

    def check(self, name):
        if name == self.name:
            return True
        if name in self.cn_name:
            return True
        return False

    def __str__(self):
        r, g, b = self.rgb
        return f"{self.name} {'/'.join(self.cn_name)} #{self.hex_value} (R:{r}, G:{g}, B:{b})"

    @property
    def bgr(self):
        return self.rgb[::-1]


class Colors(BaseEnum):
    gray = ColorInfo("Gray", ("灰色", "灰"), (128, 128, 128))

    black = ColorInfo("Black", ("纯黑", "黑"), (0, 0, 0))
    # -------------------
    red = ColorInfo("Red", ("纯红", "红"), (255, 0, 0))
    # -------------------
    lime = ColorInfo("Lime", ("柠檬", "闪光绿"), (0, 255, 0))
    green = ColorInfo("Green", ("纯绿", "绿"), (0, 200, 0))
    # -------------------
    blue = ColorInfo("Blue", ("纯蓝", "蓝"), (255, 0, 0))
    # -------------------
    yellow = ColorInfo("Yellow", ("纯黄", "黄"), (255, 255, 0))
    # -------------------
    magenta = ColorInfo("Magenta", ("洋红", "玫瑰红", "品红", "紫红"), (255, 0, 255))
    # -------------------
    cyan = ColorInfo("Cyan", ("青色", "青"), (0, 255, 255))
    # -------------------
    white = ColorInfo("White", ("纯白", "白"), (255, 255, 255))

    @classmethod
    def index(cls, name: str) -> Optional[ColorInfo]:
        name = name.rstrip("色")
        for item in cls:
            color_name, color_info = item.name, item.value
            if color_name == name or color_info.check(name):
                return color_info
        else:
            return ColorInfo(name, (name, ), (-1, -1, -1))
