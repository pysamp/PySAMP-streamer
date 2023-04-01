from pysamp import call_native_function, register_callback
from samp import INVALID_PLAYER_ID, INVALID_VEHICLE_ID


def register_callbacks():
    register_callback("OnDynamicObjectMoved", "i")
    register_callback("OnPlayerEditDynamicObject", "iiiffffff")
    register_callback("OnPlayerSelectDynamicObject", "iiifff")
    register_callback("OnPlayerShootDynamicObject", "iiifff")
    register_callback("OnPlayerPickUpDynamicPickup", "ii")
    register_callback("OnPlayerEnterDynamicCP", "ii")
    register_callback("OnPlayerLeaveDynamicCP", "ii")
    register_callback("OnPlayerEnterDynamicRaceCP", "ii")
    register_callback("OnPlayerLeaveDynamicRaceCP", "ii")
    register_callback("OnPlayerEnterDynamicArea", "ii")
    register_callback("OnPlayerLeaveDynamicArea", "ii")
    register_callback("OnPlayerGiveDamageDynamicActor", "iifii")
    register_callback("OnDynamicActorStreamIn", "ii")
    register_callback("OnDynamicActorStreamOut", "ii")
    register_callback("Streamer_OnItemStreamIn", "iii")
    register_callback("Streamer_OnItemStreamOut", "iii")
    register_callback("Streamer_OnPluginError", "s")


def get_tick_rate():
    return call_native_function("Streamer_GetTickRate")


def set_tick_rate(rate):
    return call_native_function("Streamer_SetTickRate", rate)


def get_player_tick_rate(player_id: int):
    return call_native_function("Streamer_GetPlayerTickRate", player_id)


def set_player_tick_rate(player_id: int, rate):
    return call_native_function("Streamer_SetPlayerTickRate", player_id, rate)


def toggle_chunk_stream(toggle):
    return call_native_function("Streamer_ToggleChunkStream", toggle)


def is_toggle_chunk_stream():
    return call_native_function("Streamer_IsToggleChunkStream")


def get_chunk_tick_rate(type, player_id: int = -1):
    return call_native_function("Streamer_GetChunkTickRate", type, player_id)


def set_chunk_tick_rate(type, rate, player_id: int = -1):
    return call_native_function(
        "Streamer_SetChunkTickRate", type, rate, player_id
    )


def get_chunk_size(type):
    return call_native_function("Streamer_GetChunkSize", type)


def set_chunk_size(type, size):
    return call_native_function("Streamer_SetChunkSize", type, size)


def get_max_item(type):
    return call_native_function("Streamer_GetMaxItems", type)


def set_max_items(type, items):
    return call_native_function("Streamer_SetMaxItems", type, items)


def get_visible_items(type, player_id: int = -1):
    return call_native_function("Streamer_GetVisibleItems", type, player_id)


def set_visible_items(type, items, player_id: int = -1):
    return call_native_function(
        "Streamer_SetVisibleItems", type, items, player_id
    )


def set_radius_multiplier(type, multiplier: float, player_id: int = -1):
    return call_native_function(
        "Streamer_SetRadiusMultiplier", type, multiplier, player_id
    )


def get_type_priority(types: list, maxtypes=8):
    return call_native_function("Streamer_GetTypePriority", types, maxtypes)


def set_type_priority(types: list, maxtypes=8):
    return call_native_function("Streamer_SetTypePriority", types, maxtypes)


def set_cell_distance(distance: float):
    return call_native_function("Streamer_SetCellDistance", distance)


def set_cell_size(size: float):
    return call_native_function("Streamer_SetCellSize", size)


def toggle_item_static(type, id, toggle):
    return call_native_function("Streamer_ToggleItemStatic", type, id, toggle)


def is_toggle_item_static(type, id):
    return call_native_function("Streamer_IsToggleItemStatic", type, id)


def toggle_item_inv_areas(type, id, toggle):
    return call_native_function(
        "Streamer_ToggleItemInvAreas", type, id, toggle
    )


def is_toggle_item_inv_areas(type, id, toggle):
    return call_native_function("Streamer_IsToggleItemInvAreas", type, id)


def toggle_item_callbacks(type, id, toggle):
    return call_native_function(
        "Streamer_ToggleItemCallbacks", type, id, toggle
    )


def is_toggle_item_callbacks(type, id):
    return call_native_function("Streamer_IsToggleItemCallbacks", type, id)


def toggle_error_callback(toggle):
    return call_native_function("Streamer_ToggleErrorCallback", toggle)


def is_toggle_error_callback():
    return call_native_function("Streamer_IsToggleErrorCallback")


def amx_unload_destroy_items(toggle):
    return call_native_function("Streamer_AmxUnloadDestroyItems", toggle)


# Natives (Updates)


def process_active_items():
    return call_native_function("Streamer_ProcessActiveItems")


def toggle_idle_update(player_id: int, toggle):
    return call_native_function("Streamer_ToggleIdleUpdate", player_id, toggle)


def is_toggle_idle_update(player_id: int):
    return call_native_function("Streamer_IsToggleIdleUpdate", player_id)


def toggle_camera_update(player_id: int, toggle):
    return call_native_function(
        "Streamer_ToggleCameraUpdate", player_id, toggle
    )


def is_toggle_camera_update(player_id: int):
    return call_native_function("Streamer_IsToggleCameraUpdate", player_id)


def toggle_item_updadte(player_id: int, type, toggle):
    return call_native_function(
        "Streamer_ToggleItemUpdate", player_id, type, toggle
    )


def is_toggle_item_updadte(player_id: int, type):
    return call_native_function("Streamer_IsToggleItemUpdate", player_id, type)


def update(player_id: int, type: int = -1):
    return call_native_function("Streamer_Update", player_id, type)


def update_ex(
    player_id: int,
    x: float,
    y: float,
    z: float,
    world_id: int = -1,
    interior_id: int = -1,
    type: int = -1,
    compensated_time: int = -1,
    freeze_player: int = 1,
):
    return call_native_function(
        "Streamer_UpdateEx",
        player_id,
        x,
        y,
        z,
        world_id,
        interior_id,
        type,
        compensated_time,
        freeze_player,
    )


# Natives (Data Manipulation)


def set_float_data(type, id, data, value: float):
    return call_native_function("Streamer_SetFloatData", type, id, data, value)


def get_int_data(type, id, data):
    return call_native_function("Streamer_GetIntData", type, id, data)


def set_int_data(type, id, data, value):
    return call_native_function("Streamer_SetIntData", type, id, data, value)


def remove_int_data(type, id, data):
    return call_native_function("Streamer_RemoveIntData", type, id, data)


def has_int_data(type, id, data):
    return call_native_function("Streamer_HasIntData", type, id, data)


def get_array_data(type, id, data, dest: list):
    maxdest = len(dest)
    return call_native_function(
        "Streamer_GetArrayData", type, id, dest, maxdest
    )


def set_array_data(type, id, data, scr: list):
    maxscr = len(scr)
    return call_native_function(
        "Streamer_SetArrayData", type, id, data, scr, maxscr
    )


def is_in_array_data(type, id, data, value):
    return call_native_function(
        "Streamer_IsInArrayData", type, id, data, value
    )


def append_array_data(type, id, data, value):
    return call_native_function(
        "Streamer_AppendArrayData", type, id, data, value
    )


def remove_array_data(type, id, data, value):
    return call_native_function(
        "Streamer_RemoveArrayData", type, id, data, value
    )


def has_array_data(type, id, data):
    return call_native_function("Streamer_HasArrayData", type, id, data)


def get_array_data_length(type, id, data):
    return call_native_function("Streamer_GetArrayDataLength", type, id, data)


def get_upper_bound(type):
    return call_native_function("Streamer_GetUpperBound", type)


# Natives (Miscellaneous)


def toggle_item(player_id: int, type, id, toggle):
    return call_native_function(
        "Streamer_ToggleItem", player_id, type, id, toggle
    )


def is_toggle_item(player_id: int, type, id):
    return call_native_function("Streamer_IsToggleItem", player_id, type, id)


def toggle_all_items(player_id: int, type, toggle, *exceptions):
    maxexceptions = len(exceptions)
    return call_native_function(
        "Streamer_ToggleAllItems",
        player_id,
        type,
        toggle,
        exceptions,
        maxexceptions,
    )


def get_item_internal_id(player_id: int, type, streamer_id: int):
    return call_native_function(
        "Streamer_GetItemInternalID", player_id, type, streamer_id
    )


def get_item_streamer_id(player_id: int, type, internal_id: int):
    return call_native_function(
        "Streamer_GetItemStreamerID", player_id, type, internal_id
    )


def is_item_visible(player_id: int, type, id):
    return call_native_function("Streamer_IsItemVisible", player_id, type, id)


def destroy_all_visible_items(player_id: int, type, server_wide: int = 1):
    return call_native_function(
        "Streamer_DestroyAllVisibleItems", player_id, type, server_wide
    )


def count_visible_items(player_id: int, type, server_wide: int = 1):
    return call_native_function(
        "Streamer_CountVisibleItems", player_id, type, server_wide
    )


def destroy_all_items(type, server_wide: int = 1):
    return call_native_function("Streamer_DestroyAllItems", type, server_wide)


def count_items(type, server_wide: int = 1):
    return call_native_function("Streamer_CountItems", type, server_wide)


def get_nearby_items(
    x: float,
    y: float,
    z: float,
    items: list,
    range: float = 300.0,
    world_id: int = -1,
):
    maxitems = len(items)
    return call_native_function(
        "Streamer_GetNearbyItems",
        x,
        y,
        z,
        type,
        items,
        maxitems,
        range,
        world_id,
    )


def get_all_visible_items(player_id: int, type, items: list):
    maxitems = len(items)
    return call_native_function(
        "Streamer_GetAllVisibleItems", player_id, type, items, maxitems
    )


def get_item_pos(type, id, x: float, y: float, z: float):
    return call_native_function("Streamer_GetItemPos", type, id, x, y, z)


def set_item_pos(type, id, x: float, y: float, z: float):
    return call_native_function("Streamer_SetItemPos", type, id, x, y, z)


def set_item_off_set(type, id, x: float, y: float, z: float):
    return call_native_function("Streamer_SetItemOffset", type, id, x, y, z)


# Natives (Objects)


def create_dynamic_object(
    model_id: int,
    x: float,
    y: float,
    z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    stream_distance: float = 300.0,
    draw_distance: float = 0.0,
    area_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicObject",
        model_id,
        x,
        y,
        z,
        rotation_x,
        rotation_y,
        rotation_z,
        world_id,
        interior_id,
        player_id,
        stream_distance,
        draw_distance,
        area_id,
        priority,
    )


def destroy_dynamic_object(object_id: int):
    return call_native_function("DestroyDynamicObject", object_id)


def is_valid_dynamic_object(object_id: int):
    return call_native_function("IsValidDynamicObject", object_id)


def set_dynamic_object_pos(object_id: int, x: float, y: float, z: float):
    return call_native_function("SetDynamicObjectPos", object_id, x, y, z)


def set_dynamic_object_rot(
    object_id: int, rotation_x: float, rotation_y: float, rotation_z: float
):
    return call_native_function(
        "SetDynamicObjectRot", object_id, rotation_x, rotation_y, rotation_z
    )


def get_dynamic_object_no_camera_col(object_id: int):
    return call_native_function("GetDynamicObjectNoCameraCol", object_id)


def set_dynamic_object_no_camera_col(object_id: int):
    return call_native_function("SetDynamicObjectNoCameraCol", object_id)


def move_dynamic_object(
    object_id: int,
    x: float,
    y: float,
    z: float,
    speed: float,
    rotation_x: float = -1000.0,
    rotation_y: float = -1000.0,
    rotation_z: float = -1000.0,
):
    return call_native_function(
        "MoveDynamicObject",
        object_id,
        x,
        y,
        z,
        speed,
        rotation_x,
        rotation_y,
        rotation_z,
    )


def stop_dynamic_object(object_id: int):
    return call_native_function("StopDynamicObject", object_id)


def is_dynamic_object_moving(object_id: int):
    return call_native_function("IsDynamicObjectMoving", object_id)


def attach_camera_to_dynamic_object(player_id: int, object_id: int):
    return call_native_function(
        "AttachCameraToDynamicObject", player_id, object_id
    )


def attach_dynamic_object_to_object(
    object_id: int,
    attach_to_id: int,
    offset_x: float,
    offset_y: float,
    offset_z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
    syncrotation: int = 1,
):
    return call_native_function(
        "AttachDynamicObjectToObject",
        object_id,
        attach_to_id,
        offset_x,
        offset_y,
        offset_z,
        rotation_x,
        rotation_y,
        rotation_z,
        syncrotation,
    )


def attach_dynamic_object_to_player(
    object_id: int,
    player_id: int,
    offset_x: float,
    offset_y: float,
    offset_z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
):
    return call_native_function(
        "AttachDynamicObjectToPlayer",
        object_id,
        player_id,
        offset_x,
        offset_y,
        offset_z,
        rotation_x,
        rotation_y,
        rotation_z,
    )


def attach_dynamic_object_to_vehicle(
    object_id: int,
    vehicle_id: int,
    offset_x: float,
    offset_y: float,
    offset_z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
):
    return call_native_function(
        "AttachDynamicObjectToVehicle",
        object_id,
        vehicle_id,
        offset_x,
        offset_y,
        offset_z,
        rotation_x,
        rotation_y,
        rotation_z,
    )


def edit_dynamic_object(player_id: int, object_id: int):
    return call_native_function("EditDynamicObject", player_id, object_id)


def is_dynamic_object_material_used(object_id: int, material_index):
    return call_native_function(
        "IsDynamicObjectMaterialUsed", object_id, material_index
    )


def remove_dynamic_object_material(object_id: int, material_index):
    return call_native_function(
        "RemoveDynamicObjectMaterial", object_id, material_index
    )


def set_dynamic_object_material(
    object_id: int,
    material_index: int,
    model_id: int,
    txd_name: str,
    texturename: str,
    material_color: int = 0,
):
    return call_native_function(
        "SetDynamicObjectMaterial",
        object_id,
        material_index,
        model_id,
        txd_name,
        texturename,
        material_color,
    )


def is_dynamic_object_material_text_used(object_id: int, material_index: int):
    return call_native_function(
        "IsDynamicObjectMaterialTextUsed", object_id, material_index
    )


def remove_dynamic_object_material_text(object_id: int, material_index: int):
    return call_native_function(
        "RemoveDynamicObjectMaterialText", object_id, material_index
    )


def set_dynamic_object_material_text(
    object_id: int,
    material_index: int,
    text: str,
    material_size: int = 90,
    font_face: str = "Arial",
    font_size: int = 24,
    bold: int = 1,
    font_color: int = 0xFFFFFFFF,
    back_color: int = 0,
    text_alignment: int = 0,
):
    return call_native_function(
        "SetDynamicObjectMaterialText",
        object_id,
        material_index,
        text,
        material_size,
        font_face,
        font_size,
        bold,
        font_color,
        back_color,
        text_alignment,
    )


def get_player_camera_target_dyn_object(player_id: int):
    return call_native_function("GetPlayerCameraTargetDynObject", player_id)


# Natives (Pickups)


def create_dynamic_pickup(
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
):
    return call_native_function(
        "CreateDynamicPickup",
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


def destroy_dynamic_pickup(pickup_id: int):
    return call_native_function("DestroyDynamicPickup", pickup_id)


def is_valid_dynamic_pickup(pickup_id: int):
    return call_native_function("IsValidDynamicPickup", pickup_id)


# Natives (Checkpoints)


def create_dynamic_cp(
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
):
    return call_native_function(
        "CreateDynamicCP",
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


def destroy_dynamic_cp(checkpoint_id: int):
    return call_native_function("DestroyDynamicCP", checkpoint_id)


def is_valid_dynamic_cp(checkpoint_id: int):
    return call_native_function("IsValidDynamicCP", checkpoint_id)


def is_player_in_dynamic_cp(player_id: int, checkpoint_id: int):
    return call_native_function(
        "IsPlayerInDynamicCP", player_id, checkpoint_id
    )


def get_player_visible_dynamic_cp(player_id: int):
    return call_native_function("GetPlayerVisibleDynamicCP", player_id)


# Natives (Race Checkpoints)


def create_dynamic_race_cp(
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
):
    return call_native_function(
        "CreateDynamicRaceCP",
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


def destroy_dynamic_race_cp(checkpoint_id: int):
    return call_native_function("DestroyDynamicRaceCP", checkpoint_id)


def is_valid_dynamic_race_cp(checkpoint_id: int):
    return call_native_function("IsValidDynamicRaceCP", checkpoint_id)


def is_player_in_dynamic_race_cp(player_id: int, checkpoint_id: int):
    return call_native_function(
        "IsPlayerInDynamicRaceCP", player_id, checkpoint_id
    )


def get_player_visible_dynamic_race_cp(player_id: int):
    return call_native_function("GetPlayerVisibleDynamicRaceCP", player_id)


# Natives (Map Icons)


def create_dynamic_map_icon(
    x: float,
    y: float,
    z: float,
    type: int,
    color: int,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    stream_distance: float = 200.0,
    style: int = 0,
    area_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicMapIcon",
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


def destroy_dynamic_map_icon(icon_id: int):
    return call_native_function("DestroyDynamicMapIcon", icon_id)


def is_valid_dynamic_map_icon(icon_id: int):
    return call_native_function("IsValidDynamicMapIcon", icon_id)


# Natives (3D Text Labels)


def create_dynamic_3d_text_label(
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
):
    return call_native_function(
        "CreateDynamic3DTextLabel",
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


def destroy_dynamic_3d_text_label(id: int):
    return call_native_function("DestroyDynamic3DTextLabel", id)


def is_valid_dynamic_3d_text_label(id: int):
    return call_native_function("IsValidDynamic3DTextLabel", id)


def get_dynamic_3d_text_label_text(id: int, text: str):
    maxtext = len(text)
    return call_native_function("GetDynamic3DTextLabelText", id, text, maxtext)


def update_dynamic_3d_text_label_text(id: int, color: int, text: str):
    return call_native_function(
        "UpdateDynamic3DTextLabelText", id, color, text
    )


# Natives (Areas)


def create_dynamic_circle(
    x: float,
    y: float,
    size: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicCircle",
        x,
        y,
        size,
        world_id,
        interior_id,
        player_id,
        priority,
    )


def create_dynamic_cylinder(
    x: float,
    y: float,
    min_z: float,
    max_z: float,
    size: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicCylinder",
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


def create_dynamic_sphere(
    x: float,
    y: float,
    z: float,
    size: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicSphere",
        x,
        y,
        z,
        size,
        world_id,
        interior_id,
        player_id,
        priority,
    )


def create_dynamic_rectangle(
    min_x: float,
    min_y: float,
    max_x: float,
    max_y: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicRectangle",
        min_x,
        min_y,
        max_x,
        max_y,
        world_id,
        interior_id,
        player_id,
        priority,
    )


def create_dynamic_cuboid(
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
):
    return call_native_function(
        "CreateDynamicCuboid",
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


def create_dynamic_cube(
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
):
    return call_native_function(
        "CreateDynamicCube",
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


def create_dynamic_polygon(
    points: list[float],
    min_z: float = -2139095040.0,
    max_z: float = 2139095040.0,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    priority: int = 0,
):
    max_points = len(points)
    return call_native_function(
        "CreateDynamicPolygon",
        points,
        min_z,
        max_z,
        max_points,
        world_id,
        interior_id,
        player_id,
        priority,
    )


def destroy_dynamic_area(area_id: int):
    return call_native_function("DestroyDynamicArea", area_id)


def is_valid_dynamic_area(area_id: int):
    return call_native_function("IsValidDynamicArea", area_id)


def get_dynamic_area_type(area_id: int):
    return call_native_function("GetDynamicAreaType", area_id)


def get_dynamic_polygon_points(area_id: int, points: list[float]):
    maxpoints = len(points)
    return call_native_function(
        "GetDynamicPolygonPoints", area_id, points, maxpoints
    )


def get_dynamic_polygon_number_points(area_id: int):
    return call_native_function("GetDynamicPolygonNumberPoints", area_id)


def is_player_in_dynamic_area(player_id: int, area_id: int, recheck: int = 0):
    return call_native_function(
        "IsPlayerInDynamicArea", player_id, area_id, recheck
    )


def is_player_in_any_dynamic_area(player_id: int, recheck: int = 0):
    return call_native_function("IsPlayerInAnyDynamicArea", player_id, recheck)


def is_any_player_in_dynamic_area(area_id: int, recheck: int = 0):
    return call_native_function("IsAnyPlayerInDynamicArea", area_id, recheck)


def is_any_player_in_any_dynamic_area(recheck: int = 0):
    return call_native_function("IsAnyPlayerInAnyDynamicArea", recheck)


def get_player_dynamic_areas(player_id: int, areas: list):
    maxareas = len(areas)
    return call_native_function(
        "GetPlayerDynamicAreas", player_id, areas, maxareas
    )


def get_player_number_dynamic_areas(player_id: int):
    return call_native_function("GetPlayerNumberDynamicAreas", player_id)


def is_point_in_dynamic_area(area_id: int, x: float, y: float, z: float):
    return call_native_function("IsPointInDynamicArea", area_id, x, y, z)


def is_point_in_any_dynamic_area(x: float, y: float, z: float):
    return call_native_function("IsPointInAnyDynamicArea", x, y, z)


def is_line_in_dynamic_area(
    area_id: int,
    x: float,
    y: float,
    z: float,
    x_1: float,
    y_1: float,
    z_1: float,
):
    return call_native_function(
        "IsLineInDynamicArea", area_id, x, y, z, x_1, y_1, z_1
    )


def is_line_in_any_dynamic_area(
    x: float, y: float, z: float, x_1: float, y_1: float, z_1: float
):
    return call_native_function(
        "IsLineInAnyDynamicArea", x, y, z, x_1, y_1, z_1
    )


def get_dynamic_areas_for_point(x: float, y: float, z: float, areas: list):
    maxareas = len(areas)
    return call_native_function(
        "GetDynamicAreasForPoint", x, y, z, areas, maxareas
    )


def get_number_dynamic_areas_for_point(x: float, y: float, z: float):
    return call_native_function("GetNumberDynamicAreasForPoint", x, y, z)


def get_dynamic_areas_for_line(
    x: float,
    y: float,
    z: float,
    x_1: float,
    y_1: float,
    z_1: float,
    areas: list,
):
    maxareas = len(areas)
    return call_native_function(
        "GetDynamicAreasForLine", x, y, z, x_1, y_1, z_1, areas, maxareas
    )


def get_number_dynamic_areas_for_line(
    x: float, y: float, z: float, x_1: float, y_1: float, z_1: float
):
    return call_native_function(
        "GetNumberDynamicAreasForLine", x, y, z, x_1, y_1, z_1
    )


def attach_dynamic_area_to_object(
    area_id: int,
    object_id: int,
    type: int = 2,
    player_id: int = INVALID_PLAYER_ID,
    offset_x: float = 0.0,
    offset_y: float = 0.0,
    offset_z: float = 0.0,
):
    return call_native_function(
        "AttachDynamicAreaToObject",
        area_id,
        object_id,
        type,
        player_id,
        offset_x,
        offset_y,
        offset_z,
    )


def attach_dynamic_area_to_player(
    area_id: int,
    player_id: int,
    offset_x: float = 0.0,
    offset_y: float = 0.0,
    offset_z: float = 0.0,
):
    return call_native_function(
        "AttachDynamicAreaToPlayer",
        area_id,
        player_id,
        offset_x,
        offset_y,
        offset_z,
    )


def attach_dynamic_area_to_vehicle(
    area_id: int,
    vehicle_id: int,
    offset_x: float = 0.0,
    offset_y: float = 0.0,
    offset_z: float = 0.0,
):
    return call_native_function(
        "AttachDynamicAreaToVehicle",
        area_id,
        vehicle_id,
        offset_x,
        offset_y,
        offset_z,
    )


def toggle_dyn_area_spectate_mode(area_id: int, toggle: int):
    return call_native_function("ToggleDynAreaSpectateMode", area_id, toggle)


def is_toggle_dyn_area_spectate_mode(area_id: int):
    return call_native_function("IsToggleDynAreaSpectateMode", area_id)


# Natives (Actors)


def create_dynamic_actor(
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
):
    return call_native_function(
        "CreateDynamicActor",
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
    )


def destroy_dynamic_actor(actor_id: int):
    return call_native_function("DestroyDynamicActor", actor_id)


def is_valid_dynamic_actor(actor_id: int):
    return call_native_function("IsValidDynamicActor", actor_id)


def is_dynamic_actor_streamed_in(actor_id: int, for_player_id: int):
    return call_native_function(
        "IsDynamicActorStreamedIn", actor_id, for_player_id
    )


def get_dynamic_actor_virtual_world(actor_id: int):
    return call_native_function("GetDynamicActorVirtualWorld", actor_id)


def set_dynamic_actor_virtual_world(actor_id: int, virtual_world: int):
    return call_native_function(
        "SetDynamicActorVirtualWorld", actor_id, virtual_world
    )


def get_dynamic_actor_animation(
    actor_id: int,
    anim_lib: str,
    anim_name: str,
    fdelta: float,
    loop: int,
    lock_x: int,
    lock_y: int,
    freeze: int,
    time: int,
):
    maxanimlib = len(anim_lib)
    maxanimname = len(anim_name)
    return call_native_function(
        "GetDynamicActorAnimation",
        actor_id,
        anim_lib,
        anim_name,
        fdelta,
        loop,
        lock_x,
        lock_y,
        freeze,
        time,
        maxanimlib,
        maxanimname,
    )


def apply_dynamic_actor_animation(
    actor_id: int,
    anim_lib: str,
    anim_name: str,
    fdelta: float,
    loop: int,
    lock_x: int,
    lock_y: int,
    freeze: int,
    time: int,
):
    return call_native_function(
        "ApplyDynamicActorAnimation",
        actor_id,
        anim_lib,
        anim_name,
        fdelta,
        loop,
        lock_x,
        lock_y,
        freeze,
        time,
    )


def clear_dynamic_actor_animations(actor_id: int):
    return call_native_function("ClearDynamicActorAnimations", actor_id)


def set_dynamic_actor_facing_angle(actor_id: int, angle: float):
    return call_native_function("SetDynamicActorFacingAngle", actor_id, angle)


def set_dynamic_actor_pos(actor_id: int, x: float, y: float, z: float):
    return call_native_function("SetDynamicActorPos", actor_id, x, y, z)


def set_dynamic_actor_health(actor_id: int, health: float):
    return call_native_function("SetDynamicActorHealth", actor_id, health)


def set_dynamic_actor_invulnerable(actor_id: int, invulnerable: bool = True):
    return call_native_function(
        "SetDynamicActorInvulnerable", actor_id, invulnerable
    )


def is_dynamic_actor_invulnerable(actor_id: int):
    return call_native_function("IsDynamicActorInvulnerable", actor_id)


def get_player_target_dynamic_actor(player_id: int):
    return call_native_function("GetPlayerTargetDynamicActor", player_id)


def get_player_camera_target_dyn_actor(player_id: int):
    return call_native_function("GetPlayerCameraTargetDynActor", player_id)


# Natives (Extended)


def create_dynamic_object_ex(
    model_id: int,
    x: float,
    y: float,
    z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
    stream_distance: float = 300.0,
    draw_distance: float = 0.0,
    worlds: list[int] = -1,
    interiors: list[int] = -1,
    players: list[int] = -1,
    areas: list[int] = -1,
    priority: int = 0,
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    maxareas = len(areas)
    return call_native_function(
        "CreateDynamicObjectEx",
        model_id,
        x,
        y,
        z,
        rotation_x,
        rotation_y,
        rotation_z,
        stream_distance,
        draw_distance,
        worlds,
        interiors,
        players,
        areas,
        priority,
        maxworlds,
        maxinteriors,
        maxplayers,
        maxareas,
    )


def create_dynamic_pickup_ex(
    model_id: int,
    type: int,
    x: float,
    y: float,
    z: float,
    stream_distance: float = 200.0,
    worlds: list[int] = -1,
    interiors: list[int] = -1,
    players: list[int] = -1,
    areas: list[int] = -1,
    priority: int = 0,
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    maxareas = len(areas)
    return call_native_function(
        "CreateDynamicPickupEx",
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
        maxworlds,
        maxinteriors,
        maxplayers,
        maxareas,
    )


def create_dynamic_cp_ex(
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
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    maxareas = len(areas)
    return call_native_function(
        "CreateDynamicCPEx",
        x,
        y,
        z,
        stream_distance,
        worlds,
        interiors,
        players,
        areas,
        priority,
        maxworlds,
        maxinteriors,
        maxplayers,
        maxareas,
    )


def create_dynamic_race_cp_ex(
    type,
    x: float,
    y: float,
    z: float,
    next_x: float,
    next_y: float,
    next_z: float,
    size: float,
    stream_distance: float = 200.0,
    worlds: list[int] = -1,
    interiors: list[int] = -1,
    players: list[int] = -1,
    areas: list[int] = -1,
    priority: int = 0,
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    maxareas = len(areas)
    return call_native_function(
        "CreateDynamicRaceCPEx",
        type,
        x,
        y,
        z,
        next_x,
        next_y,
        next_z,
        size,
        stream_distance,
        worlds,
        interiors,
        players,
        areas,
        priority,
        maxworlds,
        maxinteriors,
        maxplayers,
        maxareas,
    )


def create_dynamic_map_icon_ex(
    x: float,
    y: float,
    z: float,
    type: int,
    color: int,
    style: int = 0,
    stream_distance: float = 200.0,
    worlds: list[int] = -1,
    interiors: list[int] = -1,
    players: list[int] = -1,
    areas: list[int] = -1,
    priority: int = 0,
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    maxareas = len(areas)
    return call_native_function(
        "CreateDynamicMapIconEx",
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
        maxworlds,
        maxinteriors,
        maxplayers,
        maxareas,
    )


def create_dynamic_3d_text_label_ex(
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
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    maxareas = len(areas)
    return call_native_function(
        "CreateDynamic3DTextLabelEx",
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
        maxworlds,
        maxinteriors,
        maxplayers,
        maxareas,
    )


def create_dynamic_circle_ex(
    x: float,
    y: float,
    size: float,
    worlds: list[int] = -1,
    interiors: list[int] = -1,
    players: list[int] = -1,
    priority: int = 0,
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    return call_native_function(
        "CreateDynamicCircleEx",
        x,
        y,
        size,
        worlds,
        interiors,
        players,
        priority,
        maxworlds,
        maxinteriors,
        maxplayers,
    )


def create_dynamic_cylinder_ex(
    x: float,
    y: float,
    min_z: float,
    max_z: float,
    size: float,
    worlds: list[int] = -1,
    interiors: list[int] = -1,
    players: list[int] = -1,
    priority: int = 0,
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    return call_native_function(
        "CreateDynamicCylinderEx",
        x,
        y,
        min_z,
        max_z,
        size,
        worlds,
        interiors,
        players,
        priority,
        maxworlds,
        maxinteriors,
        maxplayers,
    )


def create_dynamic_sphere_ex(
    x: float,
    y: float,
    z: float,
    size: float,
    worlds: list[int] = -1,
    interiors: list[int] = -1,
    players: list[int] = -1,
    priority: int = 0,
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    return call_native_function(
        "CreateDynamicSphereEx",
        x,
        y,
        z,
        size,
        worlds,
        interiors,
        players,
        priority,
        maxworlds,
        maxinteriors,
        maxplayers,
    )


def create_dynamic_rectangle_ex(
    min_x: float,
    min_y: float,
    max_x: float,
    max_y: float,
    worlds: list[int] = -1,
    interiors: list[int] = -1,
    players: list[int] = -1,
    priority: int = 0,
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    return call_native_function(
        "CreateDynamicRectangleEx",
        min_x,
        min_y,
        max_x,
        max_y,
        worlds,
        interiors,
        players,
        priority,
        maxworlds,
        maxinteriors,
        maxplayers,
    )


def create_dynamic_cuboid_ex(
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
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    return call_native_function(
        "CreateDynamicCuboidEx",
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
        maxworlds,
        maxinteriors,
        maxplayers,
    )


def create_dynamic_cube_ex(
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
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    return call_native_function(
        "CreateDynamicCubeEx",
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
        maxworlds,
        maxinteriors,
        maxplayers,
    )


def create_dynamic_polygon_ex(
    points: list[float],
    min_z: float = -2139095040.0,
    max_z: float = 2139095040.0,
    worlds: list[int] = -1,
    interiors: list[int] = -1,
    players: list[int] = -1,
    priority: int = 0,
):
    maxpoints = len(points)
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    return call_native_function(
        "CreateDynamicPolygonEx",
        points,
        min_z,
        max_z,
        maxpoints,
        worlds,
        interiors,
        players,
        priority,
        maxworlds,
        maxinteriors,
        maxplayers,
    )


def create_dynamic_actor_ex(
    model_id: int,
    x: float,
    y: float,
    z: float,
    rotation: float,
    invulnerable: int = 1,
    health: float = 100.0,
    stream_distance: float = 200.0,
    worlds: list[int] = -1,
    interiors: list[int] = -1,
    players: list[int] = -1,
    areas: list[int] = -1,
    priority: int = 0,
):
    maxworlds = len(worlds)
    maxinteriors = len(interiors)
    maxplayers = len(players)
    maxareas = len(areas)
    return call_native_function(
        "CreateDynamicActorEx",
        model_id,
        x,
        y,
        z,
        rotation,
        invulnerable,
        health,
        stream_distance,
        worlds,
        interiors,
        players,
        areas,
        priority,
        maxareas,
        maxworlds,
        maxinteriors,
        maxplayers,
    )


# Natives (Deprecated)


def destroy_all_dynamic_object():
    return call_native_function("DestroyAllDynamicObjects")


def count_dynamic_object():
    return call_native_function("CountDynamicObjects")


def destroy_all_dynamic_pickups():
    return call_native_function("DestroyAllDynamicPickups")


def count_dynamic_pickups():
    return call_native_function("CountDynamicPickups")


def destroy_all_dynamic_cps():
    return call_native_function("DestroyAllDynamicCPs")


def count_dynamic_cps():
    return call_native_function("CountDynamicCPs")


def destroy_all_dynamic_race_cps():
    return call_native_function("DestroyAllDynamicRaceCPs")


def count_dynamic_race_cps():
    return call_native_function("CountDynamicRaceCPs")


def destroy_all_dynamic_map_icons():
    return call_native_function("DestroyAllDynamicMapIcons")


def count_dynamic_map_icons():
    return call_native_function("CountDynamicMapIcons")


def destroy_all_dynamic_3d_text_labels():
    return call_native_function("DestroyAllDynamic3DTextLabels")


def count_dynamic_3d_text_labels():
    return call_native_function("CountDynamic3DTextLabels")


def destroy_all_dynamic_areas():
    return call_native_function("DestroyAllDynamicAreas")


def count_dynamic_areas():
    return call_native_function("CountDynamicAreas")


def toggle_player_dynamic_cp(player_id: int, checkpoint_id: int, toggle: int):
    return call_native_function(
        "TogglePlayerDynamicCP", player_id, checkpoint_id, toggle
    )


def toggle_player_all_dynamic_cps(
    player_id: int, toggle: int, exceptions: list[int] = -1
):
    maxexceptions = len(exceptions)
    return call_native_function(
        "TogglePlayerAllDynamicCPs",
        player_id,
        toggle,
        exceptions,
        maxexceptions,
    )


def toggle_player_dynamic_race_cp(
    player_id: int, checkpoint_id: int, toggle: int
):
    return call_native_function(
        "TogglePlayerDynamicRaceCP", player_id, checkpoint_id, toggle
    )


def toggle_player_all_dynamic_race_cps(
    player_id: int, toggle: int, exceptions: list[int] = -1
):
    maxexceptions = len(exceptions)
    return call_native_function(
        "TogglePlayerAllDynamicRaceCPs",
        player_id,
        toggle,
        exceptions,
        maxexceptions,
    )


def toggle_player_dynamic_area(player_id: int, area_id: int, toggle: int):
    return call_native_function(
        "TogglePlayerDynamicArea", player_id, area_id, toggle
    )


def toggle_player_all_dynamic_areas(
    player_id: int, toggle: int, exceptions: list[int] = -1
):
    maxexceptions = len(exceptions)
    return call_native_function(
        "TogglePlayerAllDynamicAreas",
        player_id,
        toggle,
        exceptions,
        maxexceptions,
    )
