from .accessory import Accessory


class Inventory:
    def __init__(self):
        self.inventory = {}
        self.current_accessory = None

    def add(self, accessory: Accessory):
        self.inventory[accessory.id] = accessory

    def str(self):
        inventory_content = ''
        for accessory_id in self.inventory:
            inventory_content += self.inventory[accessory_id].str() + ' '

        return inventory_content
