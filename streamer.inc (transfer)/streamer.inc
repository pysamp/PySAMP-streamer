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
