import unittest
from interactive_objects.chest import Chest
from interactive_objects.behaviours import Behaviours, Behaviour
from accessories.inventory import Inventory


class TestStringMethods(unittest.TestCase):

    def testEvalActionIsNotNone(self):
        inventory = Inventory()
        chest = Chest("""een kist.  Probeer de kist maar
                           eens te openen.""",
                      {Behaviours.OPEN: {Behaviour.ACTIONS: ['inventory.add(Accessories.CANDLE)'],
                                         Behaviour.UTTER: """de
                                                  kist wordt geopend"""}
                       })
        self.assertIsNotNone(chest)
        actions = chest.behaviour.get(Behaviours.OPEN)[Behaviour.ACTIONS]
        self.assertIsNotNone(action)
        eval(action[0])
        print(inventory.str())

        utter = chest.behaviour.get(Behaviours.OPEN)[Behaviour.UTTER]
        self.assertIsNotNone(utter)
        print(utter)

    def testEvalActionIsEmpty(self):
        inventory = Inventory()
        chest = Chest("""een kist.  Probeer de kist maar
                           eens te openen.""",
                      {Behaviours.OPEN: {Behaviour.ACTIONS: [''], Behaviour.UTTER: """de
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
