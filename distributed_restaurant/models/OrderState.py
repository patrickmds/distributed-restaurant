from enum import Enum

class OrderState(Enum):
    WAITING=1,
    COOKING=2,
    DELIVERING=3,