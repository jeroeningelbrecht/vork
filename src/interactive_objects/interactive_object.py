
class InteractiveObject():

    def __init__(self):
        self.description = 'object'
        self.behaviour = {}
        self.health = 100
        self.dialog_id = 'object'

    def handle_behaviour(self, behaviour_id):
        if behaviour_id in self.behaviour:
            return self.behaviour.get(behaviour_id)
        else:
            return '{} doet dat niet'.format(self.description)

    def str(self):
        return '{}'.format(self.description)
