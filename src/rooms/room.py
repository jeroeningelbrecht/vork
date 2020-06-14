from interactive_objects.interactive_object import InteractiveObject
from .direction import Direction
from .room_state import RoomState
from json import JSONEncoder


class Room():

    def __init__(self, description, object: InteractiveObject,
                 up_room_id, right_room_id, back_room_id, left_room_id, room_state=RoomState.INITIAL):
        self.description = description
        self.object = object
        self.directions = {Direction.UP: up_room_id,
                           Direction.RIGHT: right_room_id,
                           Direction.BACK: back_room_id,
                           Direction.LEFT: left_room_id}
        self.room_state = room_state

    def interactiveObject(self, interactive_object_dialog_id):
        if self.object.dialog_id == interactive_object_dialog_id:
            return self.object
        else:
            return None

    def set_state(self, new_state: RoomState):
        self.room_state = new_state

    def isRequirementMet(self):
        return self.room_state == RoomState.END

    def str(self):
        if self.object:
            return '{} met daarin {}'.format(self.description,
                                             self.object.str())
        else:
            return '{}'.format(self.description)


class RoomEncoder(JSONEncoder):
    def default(self, object):
        return object.__dict__
