import unittest
import json
from rooms.room import Room, RoomEncoder
from rooms.room_state import RoomState
from rooms.room_map import RoomMap
from interactive_objects import behaviours, chest


class TestJSONSerialize(unittest.TestCase):

    def testJSONSerializeSimpleRoom(self):
        test_string = '{"description": "in een donkere gang", "object": null, "directions": {"up": "room_chest_1", "right": null, "back": null, "left": null}, "room_state": "end"}'
        room = Room(description="in een donkere gang",
                    object=None,
                    up_room_id=RoomMap.ROOM_CHEST_1,
                    right_room_id=None,
                    back_room_id=None,
                    left_room_id=None,
                    room_state=RoomState.END
                    )
        self.assertEqual(test_string, RoomEncoder().encode(room))

    def testJSONSerializeRoomWithInteractiveObject(self):
        room = Room(description="in een mooie kamer",
                    object=chest.Chest("""een kist.  Probeer de kist maar
                                              eens te openen.""",
                                       {behaviours.Behaviours.OPEN:{
                                                  behaviours.Behaviour.ACTIONS: ['invent.add(accessory.Accessories.CANDLE)', 'current_room.set_state(RoomState.END)'],
                                                  behaviours.Behaviour.UTTER: """de
                                                                          kist wordt geopend"""}
                                        }),
                    up_room_id=RoomMap.DARK_ROOM_TROLL_1,
                    right_room_id=None,
                    back_room_id=None,
                    left_room_id=None
                    )

        print(RoomEncoder().encode(room))
