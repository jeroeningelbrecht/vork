import unittest
import json

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('request.json', 'r') as json_file:
            json_request = json_file.read()
        cls._json_request = json.loads(json_request)

    def test_request(self):
        result = self._json_request.get('queryResult')
        session = self._json_request.get('session')
        self.assertIsNotNone(result)
        self.assertIsNotNone(session)

    def test_outputcontexts(self):
        context_path = '/contexts/_actions_on_google'
        result = self._json_request.get('queryResult')
        session = self._json_request.get('session')
        correct_output_context = filter(lambda outputContext:outputContext['name'] == '{}{}'.format(session,context_path), result['outputContexts'])
        self.assertIsNotNone(correct_output_context)
        print(list(correct_output_context)[0]['name'])

if __name__ == '__main__':
    unittest.main()
