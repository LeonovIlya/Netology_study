import requests
import pathlib


class YaUploader:
    token = ''

    def __init__(self, file_path):
        self.file_path = file_path

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_file(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': 'disk:/Netology/' + self.file_path.name, 'overwrite': 'true'}
        upload_link = requests.get(url, headers=headers, params=params).json()['href']
        res = requests.put(upload_link, data=open(self.file_path, 'rb'))
        res.raise_for_status()
        if res.status_code == 201:
            return 'Файл успешно загружен на Я.Диск'
        return 'Ошибка загрузки'


if __name__ == '__main__':
    ya = YaUploader(pathlib.Path('files_2_upload', 'test_file.txt'))
    print(ya.upload_file())

