import requests
import unittest

token = 'poligon_token'
false_token = 'something'


class YaFolders:
    def __init__(self, token, path):
        self.token = token
        self.url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': self.token}
        self.params = {'path': path}

    def create_folder(self):
        create_dir = requests.api.put(self.url, headers=self.headers, params=self.params)
        return create_dir.status_code

    def delete_folder(self):
        delete_dir = requests.api.delete(self.url, headers=self.headers, params=self.params)
        return delete_dir.status_code


class TestYapi(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def test_existed(self):
        self.assertEqual(YaFolders(token, 'TEST').create_folder(), 201)

    def test_new_create_in_folder(self):
        self.assertEqual(YaFolders(token, 'New_folder').create_folder(), 201)

    def test_false_token(self):
        self.assertEqual(YaFolders(false_token, 'TEST').create_folder(), 401)

    def test_false_path(self):
        self.assertEqual(YaFolders(token, 'TEST1').create_folder(), 409)

    def tearDown(self):
        print('method tearDown')
        YaFolders(token, 'TEST').delete_folder()


if __name__ == '__main__':
    unittest.main()
