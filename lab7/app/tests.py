from django.test import TestCase, Client
import random, string

class OverallTestCase(TestCase):
    def setUp(self):
        self.c=Client()

        # set asd here
        response=self.c.post('/set/asd', {'value': 'ffff'})

    def test_simple_set_get(self):
        response=self.c.get('/get/asd')
        self.assertEqual(str(response.content.decode('utf8')), 'ffff')
        response=self.c.post('/set/asd', {'value': 'tttt'})
        response = self.c.get('/get/asd')
        self.assertEqual(str(response.content.decode('utf8')), 'tttt')

    def test_long_key_value(self):
        long_key=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(300))
        long_value=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(300))
        response=self.c.post('/set/'+long_key, {'value': 'tttt'})
        # print(response.content)
        response = self.c.get('/get/'+long_key[:256])
        self.assertEqual(str(response.content.decode('utf8')), 'tttt')

        response = self.c.post('/set/rrr', {'value': long_value})
        response = self.c.get('/get/rrr')
        self.assertEqual(str(response.content.decode('utf8')), long_value[:256])

        response = self.c.post('/set/'+long_key, {'value': long_value})
        response = self.c.get('/get/'+long_key[:255])
        self.assertEqual(str(response.content.decode('utf8')), long_value[:256])

    def test_for_empty_value(self):
        response = self.c.post('/set/rrr', {'value': ''})
        response = self.c.get('/get/rrr')
        self.assertEqual(str(response.content.decode('utf8')), '')

        response = self.c.post('/set/ttt', )
        response = self.c.get('/get/ttt')
        print(response.content)
        self.assertEqual(str(response.content.decode('utf8')), 'key not found!')



