from interactive_objects import interactive_object, behaviours
from .direction import Direction
from .room_state import RoomState


class Room():

    def __init__(self, description, object: interactive_object.InteractiveObject,
                 up_room_id, right_room_id, back_room_id, left_room_id, room_state=RoomState.INITIAL, behaviour={}):
        self.description = description
        self.object = object
        self.directions = {Direction.UP: up_room_id,
                           Direction.RIGHT: right_room_id,
                           Direction.BACK: back_room_id,
                           Direction.LEFT: left_room_id}
        self.room_state = room_state
        self.behaviour = behaviour

    def handle_behaviour(self, behaviour_id):
        if behaviour_id in self.behaviour:
            actions = self.behaviour.get(behaviour_id)[behaviours.Behaviour.ACTIONS]
            utter = self.behaviour.get(behaviour_id)[behaviours.Behaviour.UTTER]
            if actions is not None:
                for action in actions:
                    eval(action)
            return utter
        else:
            return '{} doet dat niet'.format(self.description)

    def interactiveObject(self, interactive_object_dialog_id):
        if self.object.dialog_id == interactive_object_dialog_id:
            return self.object
        else:
            return None

    def get_state(self):
        return self.room_state

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
