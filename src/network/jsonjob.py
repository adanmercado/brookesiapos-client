import requests
import base64
from hashlib import sha256

from PySide6.QtCore import QObject, Signal

from core.user import User

class JsonJob(QObject):
    finished = Signal(dict)
    finished_with_error = Signal(str)

    def __init__(self, endpoint: str, user : User = None, method: str = 'GET') -> None:
        super(JsonJob, self).__init__()
        self.host = 'http://localhost:5000/api'
        self.endpoint = endpoint
        self.method = method

        self.url = self.host
        if not self.endpoint.startswith('/'):
            self.url += '/'
        self.url += self.endpoint

        self.headers = {
            'Accept': 'application/json'
        }

        if user:
            auth_data = base64.b64encode(f'{user.username}:{user.password}'.encode()).decode()
            self.headers['Authorization'] = 'Basic ' + auth_data

    def set_body(self, data: dict) -> None:
        self.data = data

    def start(self) -> None:
        print(f'Sending {self.method} request to {self.url}')
        try:
            if self.method == 'GET':
                response = requests.get(url=self.url, headers=self.headers)
            elif self.method == 'POST':
                response = requests.post(self.url, headers=self.headers, json=self.data)
            elif self.method == 'PUT':
                response = requests.put(self.url, headers=self.headers, json=self.data)
            elif self.method == 'DELETE':
                response = requests.delete(self.url, headers=self.headers)
            else:
                print('HTTP method not supported')
                self.finished_with_error.emit(self.tr('HTTP method not supported.'))
                return

            self.finished.emit(response.json())
        except requests.exceptions.HTTPError as e:
            print(f'HTTP error ocurred {e}')
            self.finished_with_error.emit(e)
        except requests.exceptions.ConnectionError as e:
            print(f'Server connection error: {e}')
            self.finished_with_error.emit(self.tr('Server connection error, please check your connection and try again.'))
        except Exception as e:
            print(f'An error ocurred, please try again later: {e}')
            self.finished_with_error.emit(self.tr('An error ocurred, please try again later.'))