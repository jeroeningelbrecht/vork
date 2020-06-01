from .behaviours import Behaviours
from .interactive_object import InteractiveObject


class Chest(InteractiveObject):

    def __init__(self):
        super().__init__()
        self.behaviour[Behaviours.OPEN] = 'we openen de kist'
        self.description = 'een kist'
