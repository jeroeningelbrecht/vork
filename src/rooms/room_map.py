from .room import Room
from interactive_objects import chest
from .direction import Direction


class RoomMap:

    BIG_HALLWAY = 'big_hallway'

    _rooms = {
      BIG_HALLWAY: Room(description="een grote hal",
                        object=chest.Chest(),
                        up_room_id='dark_alley',
                        right_room_id=None,
                        back_room_id=None,
                        left_room_id=None
                        ),
      'dark_alley': Room(description="een donkere gang",
                         object=None,
                         up_room_id=None,
                         right_room_id=None,
                         back_room_id=BIG_HALLWAY,
                         left_room_id=None
                         )
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
