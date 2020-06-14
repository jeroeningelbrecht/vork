from .accessory import Accessory


class Inventory:
    def __init__(self):
        self.inventory = {}
        self.current_accessory = None

    def add(self, accessory: Accessory):
        # this means you can only have 1 accessory of a particular kind like
        # 1 candle, or 1 sword, or ...
        print('inventory add accessory id: {}'.format(accessory.id))

        self.inventory[accessory.id] = accessory

    def str(self):
        inventory_content = ''
        for accessory_id in self.inventory:
            inventory_content += self.inventory[accessory_id].str() + ' '

        return inventory_content
