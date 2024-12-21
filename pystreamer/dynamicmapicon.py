from . import (
    create_dynamic_map_icon,
    create_dynamic_map_icon_ex,
    destroy_dynamic_map_icon,
    is_valid_dynamic_map_icon,
)
from .types import StreamerTypes


class DynamicMapIcon:
    def __init__(self, id: int) -> None:
        self.id = id

    @classmethod
    def create(
        cls,
        x: float,
        y: float,
        z: float,
        type: int,
        color: int,
        world_id: int = StreamerTypes.ANY,
        interior_id: int = StreamerTypes.ANY,
        player_id: int = StreamerTypes.ANY,
        stream_distance: float = StreamerTypes.MAP_ICON_SD,
        style: int = 0,
        area_id: int = StreamerTypes.ANY,
        priority: int = 0,
    ) -> "DynamicMapIcon":
        return cls(
            create_dynamic_map_icon(
                x,
                y,
                z,
                type,
                color,
                world_id,
                interior_id,
                player_id,
                stream_distance,
                style,
                area_id,
                priority,
            )
        )

    @classmethod
    def create_ex(
        cls,
        x: float,
        y: float,
        z: float,
        type: int,
        color: int,
        style: int = 0,
        stream_distance: float = StreamerTypes.MAP_ICON_SD,
        worlds: list[int] = [-1],
        interiors: list[int] = [-1],
        players: list[int] = [-1],
        areas: list[int] = [-1],
        priority: int = 0,
    ) -> "DynamicMapIcon":
        return cls(
            create_dynamic_map_icon_ex(
                x,
                y,
                z,
                type,
                color,
                style,
                stream_distance,
                worlds,
                interiors,
                players,
                areas,
                priority,
            )
        )

    def destroy(self):
        return destroy_dynamic_map_icon(self.id)

    def is_valid(self) -> bool:
        return is_valid_dynamic_map_icon(self.id)

from pysamp.player import Player # noqa
from pysamp.vehicle import Vehicle # noqa
