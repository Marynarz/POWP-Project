from enum import Enum

class SignalTypeEnum(Enum):
    BROADCAST = 1
    ATTACH = 2
    DETACH = 3
    PRIVSIG = 4
    KILLSIG = 5