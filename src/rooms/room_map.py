from .room import Room
from interactive_objects import chest
from .direction import Direction


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
                         left_room_id=None
                         ),
      ROOM_CHEST_1: Room(description="in een mooie kamer",
                         object=chest.Chest('een kist.  Probeer de kist maar eens te openen.'),
                         up_room_id=DARK_ROOM_TROLL_1,
                         right_room_id=None,
                         back_room_id=None,
                         left_room_id=None
                         ),
      DARK_ROOM_TROLL_1: Room(description="in een donkere kamer",
                              object=None,
                              up_room_id=BIG_HALLWAY,
                              right_room_id=None,
                              back_room_id=None,
                              left_room_id=None
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
            next_room_id = current_room.directions[direction]

            return next_room_id

    def room(room_id):
        return RoomMap._rooms[room_id]
