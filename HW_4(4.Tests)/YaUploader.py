import requests


class YaUploader:

    def __init__(self, token: str):
        self.token = token
        self.headers = {'Authorization': f'OAuth {self.token}'}
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'

    def mk_dir(self, path):
        response = requests.put(
            self.url,
            params={'path': path, 'overwrite': 'true'},
            headers=self.headers
        )
        return response.status_code

    def del_dir(self, path):
        response = requests.delete(
            self.url,
            params={'path': path, 'permanently': 'true'},
            headers=self.headers
        )
        return response

    def check_dir(self, path):
        response = requests.get(
            self.url,
            params={'path': path},
            headers=self.headers
        )
        return response.status_code
