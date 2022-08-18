from pysamp.event import event
from . import (
    create_dynamic_pickup,
    destroy_dynamic_pickup,
    is_valid_dynamic_pickup,
)


class DynamicPickup:
    def __init__(self, id) -> None:
        self.id = id

    @classmethod
    def create(
        cls,
        model_id: int,
        type: int,
        x: float,
        y: float,
        z: float,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        stream_distance: float = 200.0,
        area_id: int = -1,
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

    def destroy(self):
        return destroy_dynamic_pickup(self.id)

    def is_valid(self):
        return is_valid_dynamic_pickup(self.id)
