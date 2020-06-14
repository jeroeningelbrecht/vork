from accessories import accessory, inventory
from . import behaviours

class InteractiveObject():

    def __init__(self):
        self.description = 'object'
        self.behaviour = {}
        self.health = 100
        self.dialog_id = 'object'

    def handle_behaviour(self, behaviour_id, current_room_id):
        from rooms import room_map
        current_room = room_map.RoomMap.room(current_room_id)

        # TODO: always creating a new inventory will of course always reset the inventory

        invent = inventory.Inventory()

        if behaviour_id in self.behaviour:
            actions = self.behaviour.get(behaviour_id)[behaviours.Behaviour.ACTIONS]
            utter = self.behaviour.get(behaviour_id)[behaviours.Behaviour.UTTER]
            if actions is not None:
                eval(actions[0])

            return utter
        else:
            return '{} doet dat niet'.format(self.description)

    def str(self):
        return '{}'.format(self.description)
