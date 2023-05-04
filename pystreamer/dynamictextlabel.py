from . import (
    create_dynamic_3d_text_label,
    create_dynamic_3d_text_label_ex,
    destroy_dynamic_3d_text_label,
    is_valid_dynamic_3d_text_label,
    get_dynamic_3d_text_label_text,
    update_dynamic_3d_text_label_text,
)
from samp import INVALID_PLAYER_ID, INVALID_VEHICLE_ID


class DynamicTextLabel:
    def __init__(self, id) -> None:
        self.id = id

    @classmethod
    def create(
        cls,
        text: str,
        color: int,
        x: float,
        y: float,
        z: float,
        draw_distance: float,
        attached_player: int = INVALID_PLAYER_ID,
        attached_vehicle: int = INVALID_VEHICLE_ID,
        testlos: int = 0,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        stream_distance: float = 200.0,
        area_id: int = -1,
        priority: int = 0,
    ) -> "DynamicTextLabel":
        return cls(
            create_dynamic_3d_text_label(
                text,
                color,
                x,
                y,
                z,
                draw_distance,
                attached_player,
                attached_vehicle,
                testlos,
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
        text: str,
        color: int,
        x: float,
        y: float,
        z: float,
        draw_distance: float,
        attached_player: int = INVALID_PLAYER_ID,
        attached_vehicle: int = INVALID_VEHICLE_ID,
        testlos: int = 0,
        stream_distance: float = 200.0,
        worlds: list[int] = -1,
        interiors: list[int] = -1,
        players: list[int] = -1,
        areas: list[int] = -1,
        priority: int = 0,
    ) -> "DynamicTextLabel":
        return cls(
            create_dynamic_3d_text_label_ex(
                text,
                color,
                x,
                y,
                z,
                draw_distance,
                attached_player,
                attached_vehicle,
                testlos,
                stream_distance,
                worlds,
                interiors,
                players,
                areas,
                priority,
            )
        )

    def destroy(self):
        return destroy_dynamic_3d_text_label(self.id)

    def is_valid(self):
        return is_valid_dynamic_3d_text_label(self.id)

    def get_text(self, text: str):
        return get_dynamic_3d_text_label_text(self.id, text)

    def update_text(self, color: int, text: str):
        return update_dynamic_3d_text_label_text(self.id, color, text)

from pysamp.player import Player # noqa
from pysamp.vehicle import Vehicle # noqa
