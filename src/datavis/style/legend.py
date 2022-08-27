from .base import BaseEnum

from .info import Info


class Legends(BaseEnum):
    best = Info("best", matplotlib='best')
    upper_right = Info("upper_right", matplotlib='upper right')
    upper_left = Info("upper_left", matplotlib='upper left')
    lower_left = Info("lower_left", matplotlib='lower left')
    lower_right = Info("lower_right", matplotlib='lower right')
    right = Info("right", matplotlib='right')
    center_left = Info("center_left", matplotlib='center left')

    # center right
    # lower center
    # upper center
    # center

