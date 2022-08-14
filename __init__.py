from pysamp import call_native_function

def get_tick_rate():
    return call_native_function("Streamer_GetTickRate")

def set_tick_rate(rate):
    return call_native_function("Streamer_SetTickRate", rate)

def get_player_tick_rate(playerid: int):
    return call_native_function("Streamer_GetPlayerTickRate", playerid)

def set_player_tick_rate(playerid: int, rate): 
    return call_native_function("Streamer_SetPlayerTickRate", playerid, rate)

def toggle_chunk_stream(toggle):
    return call_native_function("Streamer_ToggleChunkStream", toggle)

def is_toggle_chunk_stream():
    return call_native_function("Streamer_IsToggleChunkStream")

def get_chunk_tick_rate(type, playerid: int = -1):
    return call_native_function("Streamer_GetChunkTickRate", type, playerid)

def set_chunk_tick_rate(type, rate, playerid: int = -1):
    return call_native_function("Streamer_SetChunkTickRate", type, rate, playerid)

def get_chunk_size(type):
    return call_native_function("Streamer_GetChunkSize", type)

def set_chunk_size(type, size):
    return call_native_function("Streamer_SetChunkSize", type, size)

def get_max_item(type):
    return call_native_function("Streamer_GetMaxItems", type)

def set_max_items(type, items):
    return call_native_function("Streamer_SetMaxItems", type, items)

def get_visible_items(type, playerid: int = -1):
    return call_native_function("Streamer_GetVisibleItems", type, playerid)

def set_visible_items(type, items, playerid: int = -1):
    return call_native_function("Streamer_SetVisibleItems", type, items, playerid)

def get_radiud_multiplier(type, multiplier: float, playerid: int = -1):
    return call_native_function("Streamer_GetRadiusMultiplier", type, multiplier, playerid)

def set_radius_multiplier(type, multiplier: float, playerid: int = -1):
    return call_native_function("Streamer_SetRadiusMultiplier", type, multiplier, playerid)

def get_type_priority(types: list, maxtypes = 8):
    return call_native_function("Streamer_GetTypePriority", types, maxtypes)

def set_type_priority(types: list, maxtypes = 8):
    return call_native_function("Streamer_SetTypePriority", types, maxtypes)

def get_cell_distance(distance: float):
    return call_native_function("Streamer_GetCellDistance", distance)

def set_cell_distance(distance: float):
    return call_native_function("Streamer_SetCellDistance", distance)

def get_cell_size(size: float):
    return call_native_function("Streamer_GetCellSize", size)

def set_cell_size(size: float):
    return call_native_function("Streamer_SetCellSize", size)

def toggle_item_static(type, id, toggle):
    return call_native_function("Streamer_ToggleItemStatic", type, id, toggle)

def is_toggle_item_static(type, id):
    return call_native_function("Streamer_IsToggleItemStatic", type, id)

def toggle_item_inv_areas(type, id, toggle):
    return call_native_function("Streamer_ToggleItemInvAreas", type, id, toggle)

def is_toggle_item_inv_areas(type, id, toggle):
    return call_native_function("Streamer_IsToggleItemInvAreas", type, id)

def toggle_item_callbacks(type, id, toggle):
    return call_native_function("Streamer_ToggleItemCallbacks", type, id, toggle)

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

def toggle_idle_update(playerid: int, toggle):
    return call_native_function("Streamer_ToggleIdleUpdate", playerid, toggle)

def is_toggle_idle_update(playerid: int):
    return call_native_function("Streamer_IsToggleIdleUpdate", playerid)

def toggle_camera_update(playerid: int, toggle):
    return call_native_function("Streamer_ToggleCameraUpdate", playerid, toggle)

def is_toggle_camera_update(playerid: int):
    return call_native_function("Streamer_IsToggleCameraUpdate", playerid)

def toggle_item_updadte(playerid: int, type, toggle):
    return call_native_function("Streamer_ToggleItemUpdate", playerid, type, toggle)

def is_toggle_item_updadte(playerid: int, type):
    return call_native_function("Streamer_IsToggleItemUpdate", playerid, type)

def get_last_update_time(time: float):
    return call_native_function("Streamer_GetLastUpdateTime", time)

def update(playerid: int, type: int = -1):
    return call_native_function("Streamer_Update", playerid, type)

def update_ex(playerid: int, x: float, y: float, z: float, world_id: int = -1, interior_id: int = -1, type: int = -1, compensated_time: int = -1, freeze_player: int = 1):
    return call_native_function("Streamer_UpdateEx", playerid, x, y, z, world_id, interior_id, type, compensated_time, freeze_player)

# Natives (Data Manipulation)

def get_float_data(type, id, data, result: float):
    return call_native_function("Streamer_GetFloatData", type, id, data, result)

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
    return call_native_function("Streamer_GetArrayData", type, id, dest, maxdest)

def set_array_data(type, id, data, scr: list):
    maxscr = len(scr)
    return call_native_function("Streamer_SetArrayData", type, id, data, scr, maxscr)

def is_in_array_data(type, id, data, value):
    return call_native_function("Streamer_IsInArrayData", type, id, data, value)

def append_array_data(type, id, data, value):
    return call_native_function("Streamer_AppendArrayData", type, id, data, value)

def remove_array_data(type, id, data, value):
    return call_native_function("Streamer_RemoveArrayData", type, id, data, value)

def has_array_data(type, id, data):
    return call_native_function("Streamer_HasArrayData", type, id, data)

def get_array_data_length(type, id, data):
    return call_native_function("Streamer_GetArrayDataLength", type, id, data)

def get_upper_bound(type):
    return call_native_function("Streamer_GetUpperBound", type)

# Natives (Miscellaneous)

def get_distance_to_item(x: float, y: float, z: float, type, id, distance: float, dimensions: int = 3):
    return call_native_function("Streamer_GetDistanceToItem", x, y, z, type, id, distance, dimensions)

def toggle_item(playerid: int, type, id, toggle):
    return call_native_function("Streamer_ToggleItem", playerid, type, id, toggle)

def is_toggle_item(playerid: int, type, id):
    return call_native_function("Streamer_IsToggleItem", playerid, type, id)

def toggle_all_items(playerid: int, type, toggle, *exceptions):
    maxexceptions = len(exceptions)
    return call_native_function("Streamer_ToggleAllItems", playerid, type, toggle, exceptions, maxexceptions)

def get_item_internal_id(playerid: int, type, streamer_id: int):
    return call_native_function("Streamer_GetItemInternalID", playerid, type, streamer_id)

def get_item_streamer_id(playerid: int, type, internal_id: int):
    return call_native_function("Streamer_GetItemStreamerID", playerid, type, internal_id)

def is_item_visible(playerid: int, type, id):
    return call_native_function("Streamer_IsItemVisible", playerid, type, id)

def destroy_all_visible_items(playerid: int, type, server_wide: int = 1):
    return call_native_function("Streamer_DestroyAllVisibleItems", playerid, type, server_wide)

def count_visible_items(playerid: int, type, server_wide: int = 1):
    return call_native_function("Streamer_CountVisibleItems", playerid, type, server_wide)

def destroy_all_items(type, server_wide: int = 1):
    return call_native_function("Streamer_DestroyAllItems", type, server_wide)

def count_items(type, server_wide: int = 1):
    return call_native_function("Streamer_CountItems", type, server_wide)

def get_nearby_items(x: float, y: float, z: float, items: list, range: float = 300.0, world_id: int = -1):
    maxitems = len(items)
    return call_native_function("Streamer_GetNearbyItems", x, y, z, type, items, maxitems, range, world_id)

def get_all_visible_items(playerid: int, type, items: list):
    maxitems = len(items)
    return call_native_function("Streamer_GetAllVisibleItems", playerid, type, items, maxitems)

def get_item_pos(type, id, x: float, y: float, z: float):
    return call_native_function("Streamer_GetItemPos", type, id, x, y, z)

def set_item_pos(type, id, x: float, y: float, z:float):
    return call_native_function("Streamer_SetItemPos", type, id, x, y, z)

def get_item_off_set(type, id, x: float, y: float, z:float):
    return call_native_function("Streamer_GetItemOffset", type, id, x, y, z)

def set_item_off_set(type, id, x: float, y: flloat, z: float):
    return call_native_function("Streamer_SetItemOffset", type, id, x, y, z)

# Natives (Objects)

def create_dynamic_object(model_id: int, x: float, y: float, z: float, rotation_x: float, rotation_y: float, rotation_z: float, world_id: int = -1, playerid: int = -1, stream_distance: float = 300.0, draw_distance: float = 0.0, areaid: int = -1, priority: int = 0):
    return call_native_function("CreateDynamicObject", model_id, x, y, z, rotation_x, rotation_y, rotation_z, world_id, playerid, stream_distance, draw_distance, areaid, priority)

def destroy_dynamic_object(object_id: int):
    return call_native_function("DestroyDynamicObject", object_id)

def is_valid_dynamic_object(object_id: int):
    return call_native_function("IsValidDynamicObject", object_id)

def get_dynamic_object_pos(object_id: int, x: float, y: float, z: float):
    return call_native_function("GetDynamicObjectPos", object_id, x, y, z)

def set_dynamic_object_pos(object_id: int, x: float, y: float, z: float):
    return call_native_function("SetDynamicObjectPos", object_id, x, y, z)

def get_dynamic_object_rot(object_id: int, rotation_x: float, rotation_y: float, rotation_z: float):
    return call_native_function("GetDynamicObjectRot", object_id, rotation_x, rotation_y, rotation_z)

def set_dynamic_object_rot(object_id: int, rotation_x: float, rotation_y: float, rotation_z: float):
    return call_native_function("SetDynamicObjectRot", object_id, rotation_x, rotation_y, rotation_z)   

def get_dynamic_object_no_camera_col(object_id: int):
    return call_native_function("GetDynamicObjectNoCameraCol", object_id)

def set_dynamic_object_no_camera_col(object_id: int):
    return call_native_function("SetDynamicObjectNoCameraCol", object_id)

def move_dynamic_object(object_id: int, x: float, y: float, z: float, speed: float, rotation_x: float = -1000.0, rotation_y: float = -1000.0, rotation_z: float = -1000.0):
    return call_native_function("MoveDynamicObject", object_id, x, y, z, speed, rotation_x, rotation_y, rotation_z)

def stop_dynamic_object(object_id: int):
    return call_native_function("StopDynamicObject", object_id)

def is_dynamic_object_moving(object_id: int):
    return call_native_function("IsDynamicObjectMoving", object_id)

def attach_camera_to_dynamic_object(playerid: int, object_id: int):
    return call_native_function("AttachCameraToDynamicObject", playerid, object_id)

def attach_dynamic_object_to_object(object_id: int, attach_to_id: int, offset_x: float, offset_y: float, offset_z: float, rotation_x: float, rotation_y: float, rotation_z: float, syncrotation: int = 1):
    return call_native_function("AttachDynamicObjectToObject", object_id, attach_to_id, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z, syncrotation)

def attach_dynamic_object_to_player(object_id: int, playerid: int, offset_x: float, offset_y: float, offset_z: float, rotation_x: float, rotation_y: float, rotation_z: float):
    return call_native_function("AttachDynamicObjectToPlayer", object_id, playerid, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z)

def attach_dynamic_object_to_vehicle(object_id: int, vehicle_id: int, offset_x: float, offset_y: float, offset_z: float, rotation_x: float, rotation_y: float, rotation_z: float):
    return call_native_function("AttachDynamicObjectToVehicle", object_id, vehicle_id, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z)

def edit_dynamic_object(playerid: int):
    return call_native_function("EditDynamicObject", playerid)

def is_dynamic_object_material_used(object_id: int, material_index):
    return call_native_function("IsDynamicObjectMaterialUsed", object_id, material_index)

def remove_dynamic_object_material(object_id: int, material_index):
    return call_native_function("RemoveDynamicObjectMaterial", object_id, material_index)

def get_dynamic_object_material(object_id: int, material_index: int, model_id: int, txd_name: str, texturename: str, material_color: int= 0):
    maxtxdname = len(txd_name)
    maxtexturename = len(texturename)
    return call_native_function("GetDynamicObjectMaterial", object_id, material_index, model_id, txd_name, texturename, material_color)

def set_dynamic_object_material(object_id: int, material_index: int, model_id: int, txd_name: str, texturename: str, material_color: int = 0):
    return call_native_function("SetDynamicObjectMaterial", object_id, material_color, model_id, txd_name, texturename, material_color)

def is_dynamic_object_material_text_used(object_id: int, material_index: int):
    return call_native_function("IsDynamicObjectMaterialTextUsed", object_id, material_index)

def remove_dynamic_object_material_text(object_id: int, material_index: int):
    return call_native_function("RemoveDynamicObjectMaterialText", object_id, material_index)

def get_dynamic_object_material_text(object_id: int, material_index: int, text: str, material_size: int, font_face: str, font_size: int, bold: int, font_color: int, back_color: int, text_alignment: int):
    return call_native_function("GetDynamicObjectMaterialText", object_id, material_index, text, material_size, font_face, font_size, bold, font_color, back_color, text_alignment)

def set_dynamic_object_material_text(object_id: int, material_index: int, text: str, material_size: int = 90, font_face: str = "Arial", font_size: int = 24, bold: int = 1, font_color: int = 0xFFFFFFFF, back_color: int = 0, text_alignment: int = 0):
    return call_native_function("SetDynamicObjectMaterialText", object_id, material_index, text, material_size, font_face, font_size, bold, font_color, back_color, text_alignment)

def get_player_camera_target_dyn_object(playerid: int):
    return call_native_function("GetPlayerCameraTargetDynObject", playerid)
