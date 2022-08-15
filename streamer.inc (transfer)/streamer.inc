/*
 * Copyright (C) 2017 Incognito
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#if defined _streamer_included
	#endinput
#endif
#define _streamer_included

#include <a_samp>

// Definitions

#define STREAMER_TYPE_OBJECT (0)
#define STREAMER_TYPE_PICKUP (1)
#define STREAMER_TYPE_CP (2)
#define STREAMER_TYPE_RACE_CP (3)
#define STREAMER_TYPE_MAP_ICON (4)
#define STREAMER_TYPE_3D_TEXT_LABEL (5)
#define STREAMER_TYPE_AREA (6)
#define STREAMER_TYPE_ACTOR (7)

#define STREAMER_AREA_TYPE_CIRCLE (0)
#define STREAMER_AREA_TYPE_CYLINDER (1)
#define STREAMER_AREA_TYPE_SPHERE (2)
#define STREAMER_AREA_TYPE_RECTANGLE (3)
#define STREAMER_AREA_TYPE_CUBOID (4)
#define STREAMER_AREA_TYPE_POLYGON (5)

#define STREAMER_OBJECT_TYPE_GLOBAL (0)
#define STREAMER_OBJECT_TYPE_PLAYER (1)
#define STREAMER_OBJECT_TYPE_DYNAMIC (2)

#define STREAMER_MAX_TYPES (8)
#define STREAMER_MAX_AREA_TYPES (6)
#define STREAMER_MAX_OBJECT_TYPES (3)

#define INVALID_STREAMER_ID (0)

#if !defined FLOAT_INFINITY
    #define FLOAT_INFINITY (Float:0x7F800000)
#endif

#if defined STREAMER_ENABLE_TAGS
	#define STREAMER_TAG_OBJECT DynamicObject
	#define STREAMER_TAG_OBJECT_ALT {DynamicObject,_}
	#define STREAMER_TAG_PICKUP DynamicPickup
	#define STREAMER_TAG_CP DynamicCP
	#define STREAMER_TAG_RACE_CP DynamicRaceCP
	#define STREAMER_TAG_MAP_ICON DynamicMapIcon
	#define STREAMER_TAG_3D_TEXT_LABEL DynamicText3D
	#define STREAMER_TAG_AREA DynamicArea
	#define STREAMER_TAG_ACTOR DynamicActor

	#define STREAMER_ALL_TAGS {DynamicObject,DynamicPickup,DynamicCP,DynamicRaceCP,DynamicMapIcon,DynamicText3D,DynamicArea,DynamicActor,_}
#else
	#define STREAMER_TAG_OBJECT _
	#define STREAMER_TAG_OBJECT_ALT _
	#define STREAMER_TAG_PICKUP _
	#define STREAMER_TAG_CP _
	#define STREAMER_TAG_RACE_CP _
	#define STREAMER_TAG_MAP_ICON _
	#define STREAMER_TAG_AREA _
	#define STREAMER_TAG_ACTOR _

	#if defined STREAMER_REMOVE_TEXT3D_TAG
		#define STREAMER_TAG_3D_TEXT_LABEL _
		#define STREAMER_ALL_TAGS _
	#else
		#if defined STREAMER_USE_DYNAMIC_TEXT3D_TAG
			#define STREAMER_TAG_3D_TEXT_LABEL DynamicText3D
			#define STREAMER_ALL_TAGS {DynamicText3D,_}
		#else
			#define STREAMER_TAG_3D_TEXT_LABEL Text3D
			#define STREAMER_ALL_TAGS {Text3D,_}
		#endif
	#endif
#endif

#if !defined STREAMER_OBJECT_SD
	#define STREAMER_OBJECT_SD 300.0
#endif
#if !defined STREAMER_OBJECT_DD
	#define STREAMER_OBJECT_DD 0.0
#endif
#if !defined STREAMER_PICKUP_SD
	#define STREAMER_PICKUP_SD 200.0
#endif
#if !defined STREAMER_CP_SD
	#define STREAMER_CP_SD 200.0
#endif
#if !defined STREAMER_RACE_CP_SD
	#define STREAMER_RACE_CP_SD 200.0
#endif
#if !defined STREAMER_MAP_ICON_SD
	#define STREAMER_MAP_ICON_SD 200.0
#endif
#if !defined STREAMER_3D_TEXT_LABEL_SD
	#define STREAMER_3D_TEXT_LABEL_SD 200.0
#endif
#if !defined STREAMER_ACTOR_SD
	#define STREAMER_ACTOR_SD 200.0
#endif

// Include File Version

public Streamer_IncludeFileVersion = 0x295;

#pragma unused Streamer_IncludeFileVersion

// Enum

enum
{
	E_STREAMER_AREA_ID,
	E_STREAMER_ATTACHED_OBJECT,
	E_STREAMER_ATTACHED_PLAYER,
	E_STREAMER_ATTACHED_VEHICLE,
	E_STREAMER_ATTACH_OFFSET_X,
	E_STREAMER_ATTACH_OFFSET_Y,
	E_STREAMER_ATTACH_OFFSET_Z,
	E_STREAMER_ATTACH_R_X,
	E_STREAMER_ATTACH_R_Y,
	E_STREAMER_ATTACH_R_Z,
	E_STREAMER_ATTACH_X,
	E_STREAMER_ATTACH_Y,
	E_STREAMER_ATTACH_Z,
	E_STREAMER_COLOR,
	E_STREAMER_DRAW_DISTANCE,
	E_STREAMER_EXTRA_ID,
	E_STREAMER_HEALTH,
	E_STREAMER_INTERIOR_ID,
	E_STREAMER_INVULNERABLE,
	E_STREAMER_MAX_X,
	E_STREAMER_MAX_Y,
	E_STREAMER_MAX_Z,
	E_STREAMER_MIN_X,
	E_STREAMER_MIN_Y,
	E_STREAMER_MIN_Z,
	E_STREAMER_MODEL_ID,
	E_STREAMER_MOVE_R_X,
	E_STREAMER_MOVE_R_Y,
	E_STREAMER_MOVE_R_Z,
	E_STREAMER_MOVE_SPEED,
	E_STREAMER_MOVE_X,
	E_STREAMER_MOVE_Y,
	E_STREAMER_MOVE_Z,
	E_STREAMER_NEXT_X,
	E_STREAMER_NEXT_Y,
	E_STREAMER_NEXT_Z,
	E_STREAMER_PLAYER_ID,
	E_STREAMER_priority: int,
	E_STREAMER_ROTATION,
	E_STREAMER_R_X,
	E_STREAMER_R_Y,
	E_STREAMER_R_Z,
	E_STREAMER_SIZE,
	E_STREAMER_STREAM_DISTANCE,
	E_STREAMER_STYLE,
	E_STREAMER_SYNC_ROTATION,
	E_STREAMER_TEST_LOS,
	E_STREAMER_TYPE,
	E_STREAMER_WORLD_ID,
	E_STREAMER_X,
	E_STREAMER_Y,
	E_STREAMER_Z
}

#define E_STREAMER_CUSTOM(%0) ((%0) | 0x40000000 & ~0x80000000)



// Natives (Extended)

native STREAMER_TAG_OBJECT:CreateDynamicObjectEx(modelid, x: float, y: float, z: float, Float:rx, Float:ry, Float:rz, stream_distance: float = STREAMER_OBJECT_SD, Float:drawdistance = STREAMER_OBJECT_DD, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, const STREAMER_TAG_AREA:areas[] = { STREAMER_TAG_AREA:-1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players, maxareas = sizeof areas);
native STREAMER_TAG_PICKUP:CreateDynamicPickupEx(modelid, type, x: float, y: float, z: float, stream_distance: float = STREAMER_PICKUP_SD, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, const STREAMER_TAG_AREA:areas[] = { STREAMER_TAG_AREA:-1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players, maxareas = sizeof areas);
native STREAMER_TAG_CP:CreateDynamicCPEx(x: float, y: float, z: float, size: float, stream_distance: float = STREAMER_CP_SD, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, const STREAMER_TAG_AREA:areas[] = { STREAMER_TAG_AREA:-1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players, maxareas = sizeof areas);
native STREAMER_TAG_RACE_CP:CreateDynamicRaceCPEx(type, x: float, y: float, z: float, Float:nextx, Float:nexty, Float:nextz, size: float, stream_distance: float = STREAMER_RACE_CP_SD, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, const STREAMER_TAG_AREA:areas[] = { STREAMER_TAG_AREA:-1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players, maxareas = sizeof areas);
native STREAMER_TAG_MAP_ICON:CreateDynamicMapIconEx(x: float, y: float, z: float, type, color, style = MAPICON_LOCAL, stream_distance: float = STREAMER_MAP_ICON_SD, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, const STREAMER_TAG_AREA:areas[] = { STREAMER_TAG_AREA:-1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players, maxareas = sizeof areas);
native STREAMER_TAG_3D_TEXT_LABEL:CreateDynamic3DTextLabelEx(const text[], color, x: float, y: float, z: float, Float:drawdistance, attachedplayer = INVALID_PLAYER_ID, attachedvehicle = INVALID_VEHICLE_ID, testlos = 0, stream_distance: float = STREAMER_3D_TEXT_LABEL_SD, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, const STREAMER_TAG_AREA:areas[] = { STREAMER_TAG_AREA:-1 }, priority: int = 0,
	maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players, maxareas = sizeof areas);
native STREAMER_TAG_AREA:CreateDynamicCircleEx(x: float, y: float, size: float, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players);
native STREAMER_TAG_AREA:CreateDynamicCylinderEx(x: float, y: float, Float:minz, Float:maxz, size: float, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players);
native STREAMER_TAG_AREA:CreateDynamicSphereEx(x: float, y: float, z: float, size: float, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players);
native STREAMER_TAG_AREA:CreateDynamicRectangleEx(Float:minx, Float:miny, Float:maxx, Float:maxy, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players);
native STREAMER_TAG_AREA:CreateDynamicCuboidEx(Float:minx, Float:miny, Float:minz, Float:maxx, Float:maxy, Float:maxz, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players);
native STREAMER_TAG_AREA:CreateDynamicCubeEx(Float:minx, Float:miny, Float:minz, Float:maxx, Float:maxy, Float:maxz, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players);
native STREAMER_TAG_AREA:CreateDynamicPolygonEx(const Float:points[], Float:minz = -FLOAT_INFINITY, Float:maxz = FLOAT_INFINITY, maxpoints = sizeof points, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players);
native STREAMER_TAG_ACTOR:CreateDynamicActorEx(modelid, x: float, y: float, z: float, Float:r, invulnerable = 1, Float:health = 100.0, stream_distance: float = STREAMER_ACTOR_SD, const worlds[] = { -1 }, const interiors[] = { -1 }, const players[] = { -1 }, const STREAMER_TAG_AREA:areas[] = { STREAMER_TAG_AREA:-1 }, priority: int = 0, maxworlds = sizeof worlds, maxinteriors = sizeof interiors, maxplayers = sizeof players, maxareas = sizeof areas);

// Natives (Deprecated)

native Streamer_CallbackHook(callback, {Float,_}:...);

native Streamer_TickRate(rate);
native Streamer_MaxItems(type, items);
native Streamer_VisibleItems(type, items, playerid: int = -1);
native Streamer_CellDistance(Float:distance);
native Streamer_CellSize(size: float);

native DestroyAllDynamicObjects();
native CountDynamicObjects();
native DestroyAllDynamicPickups();
native CountDynamicPickups();
native DestroyAllDynamicCPs();
native CountDynamicCPs();
native DestroyAllDynamicRaceCPs();
native CountDynamicRaceCPs();
native DestroyAllDynamicMapIcons();
native CountDynamicMapIcons();
native DestroyAllDynamic3DTextLabels();
native CountDynamic3DTextLabels();
native DestroyAllDynamicAreas();
native CountDynamicAreas();

native TogglePlayerDynamicCP(playerid: int, STREAMER_TAG_CP:checkpointid, toggle);
native TogglePlayerAllDynamicCPs(playerid: int, toggle, const exceptions[] = { -1 }, maxexceptions = sizeof exceptions);
native TogglePlayerDynamicRaceCP(playerid: int, STREAMER_TAG_RACE_CP:checkpointid, toggle);
native TogglePlayerAllDynamicRaceCPs(playerid: int, toggle, const exceptions[] = { -1 }, maxexceptions = sizeof exceptions);
native TogglePlayerDynamicArea(playerid: int, STREAMER_TAG_AREA:areaid, toggle);
native TogglePlayerAllDynamicAreas(playerid: int, toggle, const exceptions[] = { -1 }, maxexceptions = sizeof exceptions);

// Callbacks

forward OnDynamicObjectMoved(STREAMER_TAG_OBJECT:objectid);
forward OnPlayerEditDynamicObject(playerid: int, STREAMER_TAG_OBJECT:objectid, response, x: float, y: float, z: float, Float:rx, Float:ry, Float:rz);
forward OnPlayerSelectDynamicObject(playerid: int, STREAMER_TAG_OBJECT:objectid, modelid, x: float, y: float, z: float);
forward OnPlayerShootDynamicObject(playerid: int, weaponid, STREAMER_TAG_OBJECT:objectid, x: float, y: float, z: float);
forward OnPlayerPickUpDynamicPickup(playerid: int, STREAMER_TAG_PICKUP:pickupid);
forward OnPlayerEnterDynamicCP(playerid: int, STREAMER_TAG_CP:checkpointid);
forward OnPlayerLeaveDynamicCP(playerid: int, STREAMER_TAG_CP:checkpointid);
forward OnPlayerEnterDynamicRaceCP(playerid: int, STREAMER_TAG_RACE_CP:checkpointid);
forward OnPlayerLeaveDynamicRaceCP(playerid: int, STREAMER_TAG_RACE_CP:checkpointid);
forward OnPlayerEnterDynamicArea(playerid: int, STREAMER_TAG_AREA:areaid);
forward OnPlayerLeaveDynamicArea(playerid: int, STREAMER_TAG_AREA:areaid);
forward OnPlayerGiveDamageDynamicActor(playerid: int, STREAMER_TAG_ACTOR:actorid, Float:amount, weaponid, bodypart);
forward OnDynamicActorStreamIn(STREAMER_TAG_ACTOR:actorid, forplayerid: int);
forward OnDynamicActorStreamOut(STREAMER_TAG_ACTOR:actorid, forplayerid: int);
forward Streamer_OnItemStreamIn(type, STREAMER_ALL_TAGS:id, forplayerid: int);
forward Streamer_OnItemStreamOut(type, STREAMER_ALL_TAGS:id, forplayerid: int);
forward Streamer_OnPluginError(const error[]);
