from .info import Info
from .base import BaseEnum


class HistTypes(BaseEnum):
    bar = Info("bar", matplotlib='bar')
    step = Info("step", matplotlib='step')
    step_filled = Info("step_filled", matplotlib='stepfilled')
    # barstacked

