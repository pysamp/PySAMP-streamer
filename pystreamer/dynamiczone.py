from pysamp.event import event
from . import (
    create_dynamic_circle,
    create_dynamic_circle_ex,
    create_dynamic_cylinder,
    create_dynamic_cylinder_ex,
    create_dynamic_sphere,
    create_dynamic_sphere_ex,
    create_dynamic_rectangle,
    create_dynamic_rectangle_ex,
    create_dynamic_cuboid,
    create_dynamic_cuboid_ex,
    create_dynamic_cube,
    create_dynamic_cube_ex,
    create_dynamic_polygon,
    create_dynamic_polygon_ex,
    destroy_dynamic_area,
    is_valid_dynamic_area,
    get_dynamic_area_type,
    get_dynamic_polygon_points,
    get_dynamic_polygon_number_points,
    is_player_in_dynamic_area,
    is_player_in_any_dynamic_area,
    is_any_player_in_dynamic_area,
    is_any_player_in_any_dynamic_area,
    get_player_dynamic_areas,
    get_player_number_dynamic_areas,
    is_point_in_dynamic_area,
    is_point_in_any_dynamic_area,
    is_line_in_dynamic_area,
    is_line_in_any_dynamic_area,
    get_dynamic_areas_for_point,
    get_number_dynamic_areas_for_point,
    get_dynamic_areas_for_line,
    get_number_dynamic_areas_for_line,
    attach_dynamic_area_to_object,
    attach_dynamic_area_to_player,
    attach_dynamic_area_to_vehicle,
    toggle_dyn_area_spectate_mode,
    is_toggle_dyn_area_spectate_mode,
)
from samp import INVALID_PLAYER_ID


class DynamicZone:
    def __init__(self, id) -> None:
        self.id = id

    @classmethod
    def create_circle(
        cls,
        x: float,
        y: float,
        size: float,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_circle(
                x, y, size, world_id, interior_id, player_id, priority
            )
        )

    @classmethod
    def create_circle_ex(
        cls,
        x: float,
        y: float,
        size: float,
        worlds: list[int] = -1,
        interiors: list[int] = -1,
        players: list[int] = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_circle_ex(
                x,
                y,
                size,
                worlds,
                interiors,
                players,
                priority,
            )
        )

    @classmethod
    def create_cylinder(
        cls,
        x: float,
        y: float,
        min_z: float,
        max_z: float,
        size: float,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_cylinder(
                x,
                y,
                min_z,
                max_z,
                size,
                world_id,
                interior_id,
                player_id,
                priority,
            )
        )

    @classmethod
    def create_cylinder_ex(
        cls,
        x: float,
        y: float,
        min_z: float,
        max_z: float,
        size: float,
        worlds: list[int] = -1,
        interiors: list[int] = -1,
        players: list[int] = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_cylinder_ex(
                x,
                y,
                min_z,
                max_z,
                size,
                worlds,
                interiors,
                players,
                priority,
            )
        )

    @classmethod
    def create_sphere(
        cls,
        x: float,
        y: float,
        z: float,
        size: float,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_sphere(
                x, y, z, size, world_id, interior_id, player_id, priority
            )
        )

    @classmethod
    def create_sphere_ex(
        cls,
        x: float,
        y: float,
        z: float,
        size: float,
        worlds: list[int] = -1,
        interiors: list[int] = -1,
        players: list[int] = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_sphere_ex(
                x,
                y,
                z,
                size,
                worlds,
                interiors,
                players,
                priority,
            )
        )

    @classmethod
    def create_rectangle(
        cls,
        min_x: float,
        min_y: float,
        max_x: float,
        max_y: float,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_rectangle(
                min_x,
                min_y,
                max_x,
                max_y,
                world_id,
                interior_id,
                player_id,
                priority,
            )
        )

    @classmethod
    def create_rectangle_ex(
        cls,
        min_x: float,
        min_y: float,
        max_x: float,
        max_y: float,
        worlds: list[int] = -1,
        interiors: list[int] = -1,
        players: list[int] = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_rectangle_ex(
                min_x,
                min_y,
                max_x,
                max_y,
                worlds,
                interiors,
                players,
                priority,
            )
        )

    @classmethod
    def create_cuboid(
        cls,
        min_x: float,
        min_y: float,
        min_z: float,
        max_x: float,
        max_y: float,
        max_z: float,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_cuboid(
                min_x,
                min_y,
                min_z,
                max_x,
                max_y,
                max_z,
                world_id,
                interior_id,
                player_id,
                priority,
            )
        )

    @classmethod
    def create_cuboid_ex(
        cls,
        min_x: float,
        min_y: float,
        min_z: float,
        max_x: float,
        max_y: float,
        max_z: float,
        worlds: list[int] = -1,
        interiors: list[int] = -1,
        players: list[int] = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_cuboid_ex(
                min_x,
                min_y,
                min_z,
                max_x,
                max_y,
                max_z,
                worlds,
                interiors,
                players,
                priority,
            )
        )

    @classmethod
    def create_cube(
        cls,
        min_x: float,
        min_y: float,
        min_z: float,
        max_x: float,
        max_y: float,
        max_z: float,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_cube(
                min_x,
                min_y,
                min_z,
                max_x,
                max_y,
                max_z,
                world_id,
                interior_id,
                player_id,
                priority,
            )
        )

    @classmethod
    def create_cube_ex(
        cls,
        min_x: float,
        min_y: float,
        min_z: float,
        max_x: float,
        max_y: float,
        max_z: float,
        worlds: list[int] = -1,
        interiors: list[int] = -1,
        players: list[int] = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_cube_ex(
                min_x,
                min_y,
                min_z,
                max_x,
                max_y,
                max_z,
                worlds,
                interiors,
                players,
                priority,
            )
        )

    @classmethod
    def create_polygon(
        cls,
        points: list[float],
        min_z: float = -2139095040.0,
        max_z: float = 2139095040.0,
        world_id: int = -1,
        interior_id: int = -1,
        player_id: int = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_polygon(
                points,
                min_z,
                max_z,
                world_id,
                interior_id,
                player_id,
                priority,
            )
        )

    @classmethod
    def create_polygon_ex(
        cls,
        points: list[float],
        min_z: float = -2139095040.0,
        max_z: float = 2139095040.0,
        worlds: list[int] = -1,
        interiors: list[int] = -1,
        players: list[int] = -1,
        priority: int = 0,
    ) -> "DynamicZone":
        return cls(
            create_dynamic_polygon_ex(
                points,
                min_z,
                max_z,
                worlds,
                interiors,
                players,
                priority,
            )
        )

    def destroy(self):
        return destroy_dynamic_area(self.id)

    def is_valid(self):
        return is_valid_dynamic_area(self.id)

    def get_polygon_points(self, points: list[float]):
        return get_dynamic_polygon_points(self.id, points)

    def get_type(self):
        return get_dynamic_area_type(self.id)

    def get_polygon_number_points(self):
        return get_dynamic_polygon_number_points(self.id)

    def is_player_in_area(self, player: "Player", recheck: int = 0):
        return is_player_in_dynamic_area(player.id, self.id, recheck)

    def is_player_in_any_area(self, player: "Player", recheck: int = 0):
        return is_player_in_any_dynamic_area(player.id, recheck)

    def is_any_player_in_area(self, recheck: int = 0):
        return is_any_player_in_dynamic_area(self.id, recheck)

    def is_any_player_in_any_area(self, recheck: int = 0):
        return is_any_player_in_any_dynamic_area(recheck)

    def get_player_areas(self, player: "Player", areas: list):
        return get_player_dynamic_areas(player.id, areas)

    def get_player_number_areas(self, player: "Player"):
        return get_player_number_dynamic_areas(player.id)

    def is_point_in_area(self, area_id: int, x: float, y: float, z: float):
        return is_point_in_dynamic_area(area_id, x, y, z)

    def is_point_in_any_area(self, x: float, y: float, z: float):
        return is_point_in_any_dynamic_area(x, y, z)

    def is_line_in_area(
        self, x: float, y: float, z: float, x_1: float, y_1: float, z_1: float
    ):
        return is_line_in_dynamic_area(self.id, x, y, z, x_1, y_1, z_1)

    def is_line_in_any_dynamic_area(
        self, x: float, y: float, z: float, x_1: float, y_1: float, z_1: float
    ):
        return is_line_in_any_dynamic_area(x, y, z, x_1, y_1, z_1)

    def get_areas_for_point(self, x: float, y: float, z: float, areas: list):
        return get_dynamic_areas_for_point(x, y, z, areas)

    def get_number_areas_for_point(self, x: float, y: float, z: float):
        return get_number_dynamic_areas_for_point(x, y, z)

    def get_areas_for_line(
        self,
        x: float,
        y: float,
        z: float,
        x_1: float,
        y_1: float,
        z_1: float,
        areas: list,
    ):
        return get_dynamic_areas_for_line(x, y, z, x_1, y_1, z_1, areas)

    def get_number_areas_for_line(
        x: float, y: float, z: float, x_1: float, y_1: float, z_1: float
    ):
        return get_number_dynamic_areas_for_line(x, y, z, x_1, y_1, z_1)

    def attach_area_to_object(
        self,
        object_id: int,
        type: int = 2,
        player_id: int = INVALID_PLAYER_ID,
        offset_x: float = 0.0,
        offset_y: float = 0.0,
        offset_z: float = 0.0,
    ):
        return attach_dynamic_area_to_object(
            self.id, object_id, type, player_id, offset_x, offset_y, offset_z
        )

    def attach_area_to_player(
        self,
        player: "Player",
        offset_x: float = 0.0,
        offset_y: float = 0.0,
        offset_z: float = 0.0,
    ):
        return attach_dynamic_area_to_player(
            self.id, player.id, offset_x, offset_y, offset_z
        )

    def attach_area_to_vehicle(
        self,
        vehicle: "Vehicle",
        offset_x: float = 0.0,
        offset_y: float = 0.0,
        offset_z: float = 0.0,
    ):
        return attach_dynamic_area_to_vehicle(
            self.id, vehicle.id, offset_x, offset_y, offset_z
        )

    def toggle_area_spectate_mode(self, toggle: int):
        return toggle_dyn_area_spectate_mode(self.id, toggle)

    def is_toggle_area_spectate_mode(self):
        return is_toggle_dyn_area_spectate_mode(self.id)

    @event("OnPlayerEnterDynamicArea")
    def on_player_enter(cls, player_id: int, area_id: int):
        return (Player(player_id), cls(area_id))

    @event("OnPlayerLeaveDynamicArea")
    def on_player_leave(cls, player_id: int, area_id: int):
        return (Player(player_id), cls(area_id))

from pysamp.player import Player # noqa
from pysamp.vehicle import Vehicle # noqa
