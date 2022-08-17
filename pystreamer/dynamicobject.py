from pysamp.event import event
from . import (
    create_dynamic_object, #
    destroy_dynamic_object, #
    is_valid_dynamic_object, #
    set_dynamic_object_pos, #
    set_dynamic_object_rot, #
    get_dynamic_object_no_camera_col, #
    set_dynamic_object_no_camera_col, #
    move_dynamic_object, #
    stop_dynamic_object, #
    is_dynamic_object_moving, #
    attach_camera_to_dynamic_object, #
    attach_dynamic_object_to_object, #
    attach_dynamic_object_to_player, #
    attach_dynamic_object_to_vehicle, #
    is_dynamic_object_material_used, #
    remove_dynamic_object_material, #
    set_dynamic_object_material, #
    is_dynamic_object_material_text_used, #
    remove_dynamic_object_material_text, #
    set_dynamic_object_material_text, #
)
from typing import Tuple

class DynamicObject():
    def __init__(self, id, x, y, z, rotation_x, rotation_y, rotation_z, model_id) -> None:
        self.id = id 
        self.x = x 
        self.y = y 
        self.z = z 
        self.rotation_x = rotation_x
        self.rotation_y = rotation_y
        self.rotation_z = rotation_z
        self.model_id = model_id

    @classmethod
    def create(cls, model_id: int, x: float, y: float, z: float, rotation_x: float, rotation_y: float, rotation_z: float, world_id: int = -1, interior_id: int = -1, player_id: int = -1, stream_distance: float = 300.0, draw_distance: float = 0.0, area_id: int = -1, priority = 0):
        return cls(create_dynamic_object(
            model_id, x, y, z, rotation_x, rotation_y, rotation_z, world_id, interior_id, player_id, stream_distance, draw_distance, area_id, priority
            ), x, y, z, rotation_x, rotation_y, rotation_z, model_id)

    def destroy(self):
        return destroy_dynamic_object(self.id)

    def is_valid(self):
        return is_valid_dynamic_object(self.id)

    def set_postition(self, x: float, y: float, z: float):
        self.x = x 
        self.y = y 
        self.z = z
        return set_dynamic_object_pos(self.id, x, y, z)

    def get_position(self) -> Tuple[float, float, float]:
        return self.x, self.y, self.z

    def set_rotation(self, rotation_x: float, rotation_y: float, rotation_z: float):
        self.rotation_x = rotation_x
        self.rotation_y = rotation_y
        self.rotation_z = rotation_z
        return set_dynamic_object_rot(self.id, rotation_x, rotation_y, rotation_z)

    def get_rotation(self) -> Tuple[float, float, float]:
        return self.rotation_x, self.rotation_y, self.rotation_z

    def get_no_camera_col(self):
        return get_dynamic_object_no_camera_col(self.id)

    def set__no_camera_col(self):
        return set_dynamic_object_no_camera_col(self.id)

    def move(object_id: int, x: float, y: float, z: float, speed: float, rotation_x: float = -1000.0, rotation_y: float = -1000.0, rotation_z: float = -1000.0):
        return move_dynamic_object(object_id, x, y, z, speed, rotation_x, rotation_y. rotation_z)

    def stop(self):
        return stop_dynamic_object(self.id)

    def is_moving(self):
        return is_dynamic_object_moving(self.id)

    def attach_camera_to_object(player: "Player", object_id: int):
        return attach_camera_to_dynamic_object(player.id, self.id)

    def attach_to_object(self, attach: "DynamicObject", offset_x: float, offset_y: float, offset_z: float, rotation_x: float, rotation_y: float, rotation_z: float, syncrotation: int = 1):
        return attach_dynamic_object_to_object(self.id, attach.id, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z, syncrotation)

    def attach_to_player(self, player: "Player", offset_x: float, offset_y: float, offset_z: float, rotation_x: float, rotation_y: float, rotation_z: float):
        return attach_dynamic_object_to_player(self.id, player.id, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z)

    def attach_to_vehicle(self, vehicle: "Vehicle", offset_x: float, offset_y: float, offset_z: float, rotation_x: float, rotation_y: float, rotation_z: float, syncrotation: int = 1):
        return attach_dynamic_object_to_vehicle(self.id, vehicle.id, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z, syncrotation)

    def is_material_used(self, material_index: int):
        return is_dynamic_object_material_used(self.id, material_index)

    def remove_material(self, material_index: int):
        return remove_dynamic_object_material(self.id, material_index)

    def set_material(self, material_index: int, model_id: int, txd_name: int, texturename: int, material_color: int = 0):
        return set_dynamic_object_material(self.id, material_index, model_id, txd_name, texturename, material_color)

    def is_material_text_used(self, material_index: int):
        return is_dynamic_object_material_text_used(self.id, material_index)

    def remove_material_text(self, material_index: int):
        return remove_dynamic_object_material_text(self.id, material_index)

    def set_material_text(self, material_index: int, text: str, material_size: int = 90, font_face: str = "Arial", font_size: int = 24, bold: int = 1, font_color: int = 0xFFFFFFFF, back_color: int = 0, text_alignment: int = 0):
        return set_dynamic_object_material_text(self.id, material_index, text, material_size, font_face, font_size, bold, font_color, back_color, text_alignment)
    