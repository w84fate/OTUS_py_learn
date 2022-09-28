"""
create dataclass `Engine`
"""
from dataclasses import dataclass

@dataclass()
class Engine:
    volume: float
    pistons: int

    def __post_init__(self):
        if not isinstance(self.volume, float):
            raise ValueError('value not an float')
        if not isinstance(self.pistons, int):
            raise ValueError('value not an int')