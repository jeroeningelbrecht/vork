
class Accessory:

    def __init__(self, id, description):
        self.id = id
        self.description = description

    def str(self):
        return self.description


class Accessories():
    CANDLE = Accessory(id="candle", description="een kaars")
    KNIFE = Accessory(id="knife", description="een mes")
    SWORD = Accessory(id="sword", description="een zwaard")
