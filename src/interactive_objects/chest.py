from .interactive_object import InteractiveObject


class Chest(InteractiveObject):

    def __init__(self, description, behaviour):
        super().__init__()
        self.behaviour = behaviour
        self.description = description
        self.dialog_id = 'chest'
