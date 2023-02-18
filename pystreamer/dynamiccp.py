from pysamp.event import event
from . import (
    create_dynamic_cp,
    create_dynamic_cp_ex,
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
        cls,
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

    @classmethod
    def create_ex(
        cls,
        x: float,
        y: float,
        z: float,
        size: float,
        stream_distance: float = 200.0,
        worlds: list[int] = -1,
        interiors: list[int] = -1,
        players: list[int] = -1,
        areas: list[int] = -1,
        priority: int = 0,
    ) -> "DynamicCheckpoint":
        return cls(
            create_dynamic_cp_ex(
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
        return destroy_dynamic_cp(self.id)

    def is_valid(self):
        return is_valid_dynamic_cp(self.id)

    def toggle_player(self, player: "Player", toggle: int):
        return toggle_player_dynamic_cp(player.id, self.id, toggle)

    def toggle_player_all(self, player: "Player", toggle: int):
        return toggle_player_all_dynamic_cps(player.id, toggle)

    def is_player_in(self, player: "Player"):
        return is_player_in_dynamic_cp(player.id, self.id)

    def get_player_visible(self, player: "Player"):
        return get_player_visible_dynamic_cp(player.id)

    @event("OnPlayerEnterDynamicCP")
    def on_player_enter(cls, player_id: int, checkpoint_id: int):
        return (Player(player_id), cls(checkpoint_id))

    @event("OnPlayerLeaveDynamicCP")
    def on_player_leave(cls, player_id: int, checkpoint_id: int):
        return (Player(player_id), cls(checkpoint_id))

from pysamp.player import Player # noqa
from pysamp.vehicle import Vehicle # noqa
