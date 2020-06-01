
class InteractiveObject():

    def __init__(self):
        self.description = 'object'
        self.behaviour = {}
        self.health = 100

    def handle_behaviour(self, behaviour):
        if behaviour in self.behaviour:
            return 'hallo'
        else:
            return '{} doet dat niet'.format(self.description)

    def str(self):
        return '{}'.format(self.description)
