import unittest
from src.interactive_objects.chest import Chest
from src.interactive_objects.behaviours import Behaviours
from src.accessories.inventory import Inventory
from src.accessories.accessory import Accessories


class TestStringMethods(unittest.TestCase):

    def testEvalActionIsNotNone(self):
        inventory = Inventory()
        chest = Chest("""een kist.  Probeer de kist maar
                           eens te openen.""",
                      {Behaviours.OPEN: {'action': 'inventory.add(Accessories.CANDLE)',
                                         'utter': """de
                                                  kist wordt geopend"""}
                       })
        self.assertIsNotNone(chest)
        action = chest.behaviour.get(Behaviours.OPEN)['action']
        self.assertIsNotNone(action)
        eval(action)
        print(inventory.str())

        utter = chest.behaviour.get(Behaviours.OPEN)['utter']
        self.assertIsNotNone(utter)
        print(utter)

    def testEvalActionIsEmpty(self):
        inventory = Inventory()
        chest = Chest("""een kist.  Probeer de kist maar
                           eens te openen.""",
                      {Behaviours.OPEN: {'action': '', 'utter': """de
                                                  kist wordt geopend"""}
                       })
        self.assertIsNotNone(chest)
        action = chest.behaviour.get(Behaviours.OPEN)['action']
        self.assertEqual(action, '')

        utter = chest.behaviour.get(Behaviours.OPEN)['utter']
        self.assertIsNotNone(utter)
        print(utter)


if __name__ == '__main__':
    unittest.main()
