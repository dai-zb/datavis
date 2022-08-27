from .base import BaseEnum


from .info import Info


class Markers(BaseEnum):
    point = Info("point", matplotlib=".")
    pixel = Info("pixel", matplotlib=",")
    circle = Info("circle", matplotlib="o")
    octagon = Info("octagon", matplotlib="8")

    square = Info("square", matplotlib="s")
    pentagon = Info("pentagon", matplotlib="p")
    star = Info("star", matplotlib="*")
    hexagon = Info("hexagon", matplotlib="h")
    hexagon2 = Info("hexagon2", matplotlib="H")

    plus = Info("plus", matplotlib="+")
    cross = Info("cross", matplotlib="x")

    diamond = Info("diamond", matplotlib="D")
    thin_diamond = Info("thin_diamond", matplotlib="d")

    triangle_down = Info("triangle_down", matplotlib="v")
    triangle_up = Info("triangle_up", matplotlib="^")
    triangle_left = Info("triangle_left", matplotlib="<")
    triangle_right = Info("triangle_right", matplotlib=">")

    tri_down = Info("tri_down", matplotlib="1")
    tri_up = Info("tri_up", matplotlib="2")
    tri_left = Info("tri_left", matplotlib="3")
    tri_right = Info("tri_right", matplotlib="4")
