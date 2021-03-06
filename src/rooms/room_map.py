from .room import Room
from interactive_objects import chest, behaviours
from .direction import Direction
from .room_state import RoomState


class RoomMap:

    OUTSIDE = 'outside'
    DARK_ALLEY_1 = 'dark_alley_1'
    ROOM_CHEST_1 = 'room_chest_1'
    DARK_ROOM_TROLL_1 = 'dark_room_troll_1'
    BIG_HALLWAY = 'big_hallway'

    _rooms = {
      OUTSIDE: Room(description="buiten",
                    object=None,
                    up_room_id=DARK_ALLEY_1,
                    right_room_id=None,
                    back_room_id=None,
                    left_room_id=None
                    ),
      DARK_ALLEY_1: Room(description="in een donkere gang",
                         object=None,
                         up_room_id=ROOM_CHEST_1,
                         right_room_id=None,
                         back_room_id=None,
                         left_room_id=None,
                         room_state=RoomState.END
                         ),
      ROOM_CHEST_1: Room(description="in een mooie kamer",
                         object=chest.Chest("""een kist.  Probeer de kist maar
                                            eens te openen.""",
                                            {behaviours.Behaviours.OPEN:{
                                                behaviours.Behaviour.ACTIONS: ['inventory.add(accessory.Accessories.CANDLE)', 'current_room.set_state(room_state.RoomState.END)'],
                                                behaviours.Behaviour.UTTER: """de
                                                                        kist wordt geopend"""}
                                             }),
                         up_room_id=DARK_ROOM_TROLL_1,
                         right_room_id=None,
                         back_room_id=None,
                         left_room_id=None
                         ),
      DARK_ROOM_TROLL_1: Room(description="een donkere kamer met daarin een trol maar daarover later meer",
                              object=None,
                              up_room_id=None,
                              right_room_id=BIG_HALLWAY,
                              back_room_id=None,
                              left_room_id=None,
                              behaviour={behaviours.Behaviours.LIGHT: {
                                  behaviours.Behaviour.ACTIONS: ['self.set_state(RoomState.END)'],
                                  behaviours.Behaviour.UTTER: 'het licht gaat aan'}
                               }
                              ),
      BIG_HALLWAY: Room(description="in een grote hal",
                        object=None,
                        up_room_id='dark_alley',
                        right_room_id=None,
                        back_room_id=None,
                        left_room_id=None
                        ),
    }

    def next_room_id(direction, current_room_id):
        if direction not in [Direction.UP, Direction.LEFT,
                             Direction.BACK, Direction.RIGHT]:
            return None
        else:
            current_room = RoomMap._rooms[current_room_id]
            if current_room.isRequirementMet():
                next_room_id = current_room.directions[direction]
            else:
                next_room_id = current_room_id
            return next_room_id

    def room(room_id):
        return RoomMap._rooms[room_id]
