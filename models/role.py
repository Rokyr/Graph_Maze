from enum import IntEnum, auto
#intEnum is a subclass of integer

class Role(IntEnum):
    NONE = 0
    ENEMY = auto()
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()

