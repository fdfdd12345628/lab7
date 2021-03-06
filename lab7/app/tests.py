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
        response = self.c.get('/get/'+long_key[:256])
        self.assertEqual(str(response.content.decode('utf8')), long_value[:256])

    def test_for_empty_value(self):
        response = self.c.post('/set/rrr', {'value': ''})
        response = self.c.get('/get/rrr')
        self.assertEqual(str(response.content.decode('utf8')), '')

        response = self.c.post('/set/ttt', )
        response = self.c.get('/get/ttt')
        print(response.content)
        self.assertEqual(str(response.content.decode('utf8')), 'key not found!')

    def test_for_utf8_value(self):
        key='我是中文來坑人'
        value='哈哈哈哈哈哈哈'
        response = self.c.post('/set/'+key, {'value': value})
        response = self.c.get('/get/'+key)
        self.assertEqual(str(response.content.decode('utf8')), value)

    def test_for_space_value(self):
        key='我 是 中 文 來 坑 人'
        value='哈 哈 哈 哈 哈 哈 哈'
        response = self.c.post('/set/'+key, {'value': value})
        response = self.c.get('/get/'+key)
        self.assertEqual(str(response.content.decode('utf8')), value)
        # %0A%E0%B9%84%E0%B8%95%E0%B9%89%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%99%20%5Cn%5Cn%20%5Ct%5Ct%0A%0Ai%5C%2F%3C%3E%3F%2C.%2F%3A%27%22%3B%40%23%24%25%5E%26%29%28%2B-%60~%7C%D0%A2%D0%B0%D0%B9%D0%B2%D0%B0%D0%BD%D1%8C
