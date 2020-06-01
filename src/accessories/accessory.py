
class Accessory:

    def __init__(self, id, description):
        self.id = id
        self.description = description

    def str(self):
        return self.description


CANDLE = Accessory(id="kaars", description="een kaars")
KNIVE = Accessory(id="mes", description="een mes")
SWORD = Accessory(id="zwaard", description="een zwaard")
