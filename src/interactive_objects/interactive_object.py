
class InteractiveObject():

    def __init__(self):
        self.description = 'object'
        self.behaviour = {}
        self.health = 100
        self.dialog_id = 'object'

    def handle_behaviour(self, behaviour):
        if behaviour in self.behaviour:
            return self.behaviour.get(behaviour)
        else:
            return '{} doet dat niet'.format(self.description)

    def str(self):
        return '{}'.format(self.description)
