from enum import Enum


class StreamerTypes(int, Enum):
    INVALID_ID: int = 0
    ANY: int = -1
    OBJECT_SD: float = 300.0
    OBJECT_DD: float = 0.0
    PICKUP_SD: float = 200.0
    CP_SD: float = 200.0
    RACE_CP_SD: float = 200.0
    MAP_ICON_SD: float = 200.0
    TEXT_LABEL_SD: float = 200.0
    ACTOR_SD: float = 200.0

