from enum import Enum
from typing import Optional

from .info import Info


class BaseEnum(Enum):
    @classmethod
    def index(cls, name: str) -> Optional[Info]:
        for item in cls:
            _name, _info = item.name, item.value
            if _name == name:
                return _info
        else:
            return Info(name, matplotlib=name)
