from .base import BaseEnum

from .info import Info


class LineStyles(BaseEnum):
    point = Info("solid", matplotlib="solid", matplotlib_symbol="-")
    dotted = Info("dotted", matplotlib="dotted", matplotlib_symbol="--")
    dashed = Info("dashed", matplotlib="dashed", matplotlib_symbol="-.")
    dash_dot = Info("dash_dot", matplotlib="dashdot", matplotlib_symbol=":")
