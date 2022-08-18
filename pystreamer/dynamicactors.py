from . import (
    create_dynamic_actor,
    destroy_dynamic_actor,
    is_valid_dynamic_actor,
    is_dynamic_actor_streamed_in,
    get_dynamic_actor_virtual_world,
    set_dynamic_actor_virtual_world,
    apply_dynamic_actor_animation,
    clear_dynamic_actor_animations,
    set_dynamic_actor_facing_angle,
    set_dynamic_actor_pos,
    set_dynamic_actor_health,
    set_dynamic_actor_invulnerable,
    is_dynamic_actor_invulnerable,
    get_player_target_dynamic_actor,
    get_player_camera_target_dyn_actor,
)
from typing import Tuple


class DynamicActor:
    def __init__(self, id, x, y, z, rotation, health) -> None:
        self.id = id
        self._x = x
        self._y = y
        self._z = z
        self._rotation = rotation
        self._health = health

    @classmethod
    def create(
        cls,
        model_id: int,
        x: float,
        y: float,
        z: float,
        rotation: float,
        invulnerable: bool = True,
        health: float = 100.0,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        stream_distance: float = 200.0,
        area_id: int = -1,
        priority: int = 0,
    ) -> "DynamicActor":
        return cls(
            create_dynamic_actor(
                model_id,
                x,
                y,
                z,
                rotation,
                invulnerable,
                health,
                world_id,
                interior_id,
                player_id,
                stream_distance,
                area_id,
                priority,
            ),
            x,
            y,
            z,
            rotation,
            health,
        )

    def destroy(self):
        return destroy_dynamic_actor(self.id)

    def is_valid(self):
        return is_valid_dynamic_actor(self.id)

    def is_streamed_in(self, for_player_id: int):
        return is_dynamic_actor_streamed_in(self.id, for_player_id)

    def get_virtual_world(self):
        return get_dynamic_actor_virtual_world(self.id)

    def set_virtual_world(self, virtual_world: int):
        return set_dynamic_actor_virtual_world(self.id, virtual_world)

    def apply_animation(
        self,
        anim_lib: str,
        anim_name: str,
        fdelta: float,
        loop: int,
        lock_x: int,
        lock_y: int,
        freeze: int,
        time: int,
    ):
        return apply_dynamic_actor_animation(self.id)

    def clear_animations(self):
        return clear_dynamic_actor_animations(self.id)

    def get_facing_angle(self):
        return self._rotation

    def set_facing_angle(self, angle: float):
        self._rotation = angle
        return set_dynamic_actor_facing_angle(self.id, angle)

    def get_position(self) -> Tuple[float, float, float]:
        return self._x, self._y, self._z

    def set_position(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z
        return set_dynamic_actor_pos(self.id, x, y, z)

    def get_health(self):
        return self._health

    def set_health(self, health: float):
        self._health = health
        return set_dynamic_actor_health(self.id, health)

    def set_invulnerable(self, invulnerable: bool = True):
        return set_dynamic_actor_invulnerable(self.id, invulnerable)

    def is_invulnerable(self):
        return is_dynamic_actor_invulnerable(self.id)

    def get_player_target(self, player_id: int):
        return get_player_target_dynamic_actor(player_id)

    def get_player_camera_target(self, player_id: int):
        return get_player_camera_target_dyn_actor(player_id)
