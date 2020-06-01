from interactive_objects.interactive_object import InteractiveObject
from .direction import Direction


class Room():

    def __init__(self, description, object: InteractiveObject,
                 up_room_id, right_room_id, back_room_id, left_room_id):
        self.description = description
        self.object = object
        self.directions = {Direction.UP: up_room_id,
                           Direction.RIGHT: right_room_id,
                           Direction.BACK: back_room_id,
                           Direction.LEFT: left_room_id}

    def interactiveObject(self, interactive_object_dialog_id):
        if self.object.dialog_id == interactive_object_dialog_id:
            return self.object
        else:
            return None

    def str(self):
        if self.object:
            return '{} met daarin {}'.format(self.description,
                                             self.object.str())
        else:
            return '{}'.format(self.description)
