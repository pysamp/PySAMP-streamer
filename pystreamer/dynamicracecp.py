from . import (
    create_dynamic_race_cp,
    destroy_dynamic_race_cp,
    is_valid_dynamic_race_cp,
    toggle_player_dynamic_race_cp,
    toggle_player_all_dynamic_race_cp,
    is_player_in_dynamic_race_cp,
    get_player_visible_dynamic_race_cp,
)


class DynamicRaceChecpoint:
    def __init__(self, id) -> None:
        self.id = id

    @classmethod
    def create(
        cls,
        type,
        x: float,
        y: float,
        z: float,
        next_x: float,
        next_y: float,
        next_z: float,
        size: float,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        stream_distance: float = 200.0,
        area_id: int = -1,
        priority: int = 0,
    ) -> "DynamicRaceCheckpoint":
        return cls(
            create_dynamic_race_cp(
                type,
                x,
                y,
                z,
                next_x,
                next_y,
                next_z,
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
        return destroy_dynamic_race_cp(self.id)

    def is_valid(self):
        return is_valid_dynamic_race_cp(self.id)

    def toggle_player(self, player_id: int, toggle: int):
        return toggle_player_dynamic_race_cp(player_id, self.id, toggle)

    def toggle_player_all(
        self, player_id: int, toggle: int, exceptions: list[int] = -1
    ):
        return toggle_player_all_dynamic_race_cp(player_id, toggle, exceptions)

    def is_player_in(self, player_id: int):
        return is_player_in_dynamic_race_cp(player_id, self.id)

    def get_player_visible(self, player_id: int):
        return get_player_visible_dynamic_race_cp(player_id)
