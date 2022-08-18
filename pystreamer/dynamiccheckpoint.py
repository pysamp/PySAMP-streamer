from pysamp.event import event
from . import (
    create_dynamic_cp,
    destroy_dynamic_cp,
    is_valid_dynamic_cp,
    toggle_player_dynamic_cp,
    toggle_player_all_dynamic_cps,
    is_player_in_dynamic_cp,
    get_player_visible_dynamic_cp,
)


class DynamicCheckpoint:
    def __init__(self, id) -> None:
        self.id = id

    @classmethod
    def create(
        x: float,
        y: float,
        z: float,
        size: float,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        stream_distance: float = 200.0,
        area_id: int = -1,
        priority: int = 0,
    ) -> "DynamicCheckpoint":
        return cls(
            create_dynamic_cp(
                x,
                y,
                z,
                size,
                world_id,
                interior_id,
                player_id,
                stream_distance,
                area_id,
                priority,
            )
        )

    def destroy(self):
        return destroy_dynamic_cp(self.id)

    def is_valid(self):
        return is_valid_dynamic_cp(self.id)

    def toggle_player(self, player_id: int, toggle: int):
        return toggle_player_dynamic_cp(player_id, self.id, toggle)

    def toggle_player_all(self, player_id: int, toggle: int):
        return toggle_player_all_dynamic_cps(player_id, toggle)

    def is_player_in(self, player_id: int):
        return is_player_in_dynamic_cp(player_id, self.id)

    def get_player_visible(self, player_id: int):
        return get_player_visible_dynamic_cp(player_id)
