import requests
import unittest

class TestYandexDiskAPI(unittest.TestCase):
    TOKEN = "Ваш_токен_здесь"
    API_BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

    def setUp(self):
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"OAuth {self.TOKEN}"})

    def tearDown(self):
        self.session.close()

    def test_create_folder(self):
        folder_path = "/test_folder"
        response = self.session.put(f"{self.API_BASE_URL}?path={folder_path}")
        self.assertEqual(response.status_code, 201)

        response = self.session.get(f"{self.API_BASE_URL}?path={folder_path}")
        self.assertEqual(response.status_code, 200)

    def test_create_folder_without_token(self):
        session = requests.Session()
        folder_path = "/test_folder"
        response = session.put(f"{self.API_BASE_URL}?path={folder_path}")
        self.assertEqual(response.status_code, 401)

if __name__ == "__main__":
    unittest.main()
