from pysamp.event import event
from . import (
    create_dynamic_pickup,
    create_dynamic_pickup_ex,
    destroy_dynamic_pickup,
    is_valid_dynamic_pickup,
)
from .types import StreamerTypes
from typing import Optional


class DynamicPickup:
    def __init__(self, id: int) -> None:
        self.id = id

    @classmethod
    def create(
        cls,
        model_id: int,
        type: int,
        x: float,
        y: float,
        z: float,
        world_id: int = StreamerTypes.ANY,
        interior_id: int =  StreamerTypes.ANY,
        player_id: int =  StreamerTypes.ANY,
        stream_distance: float = StreamerTypes.PICKUP_SD,
        area_id: int =  StreamerTypes.ANY,
        priority: int = 0,
    ) -> "DynamicPickup":
        return cls(
            create_dynamic_pickup(
                model_id,
                type,
                x,
                y,
                z,
                world_id,
                interior_id,
                player_id,
                stream_distance,
                area_id,
                priority,
            )
        )

    @classmethod
    def create_ex(
        cls,
        model_id: int,
        type: int,
        x: float,
        y: float,
        z: float,
        stream_distance: float = StreamerTypes.PICKUP_SD,
        worlds: Optional[list[int]] = None,
        interiors: Optional[list[int]] = None,
        players: Optional[list[int]] = None,
        areas: Optional[list[int]] = None,
        priority: int = 0,
    ) -> "DynamicPickup":
        return cls(
            create_dynamic_pickup_ex(
                model_id,
                type,
                x,
                y,
                z,
                stream_distance,
                worlds,
                interiors,
                players,
                areas,
                priority,
            )
        )

    def destroy(self):
        return destroy_dynamic_pickup(self.id)

    def is_valid(self) -> bool:
        return is_valid_dynamic_pickup(self.id)

    @event("OnPlayerPickUpDynamicPickup")
    def on_player_pick_up(cls, player_id: int, pickup_id: int):
        return (Player(player_id), cls(pickup_id))

from pysamp.player import Player # noqa
from pysamp.vehicle import Vehicle # noqa
