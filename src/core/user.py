from __future__ import annotations
from unicodedata import name

class User:
    name: str
    address : str
    phone: str
    email: str
    username: str
    password: str
    role: int

    def __init__(self) -> None:
        self.name = ''
        self.address = ''
        self.phone = ''
        self.email = ''
        self.username = ''
        self.password = ''
        self.role = 0
    
    @staticmethod
    def from_json(data: dict) -> User:
        print(data)
        user = User()
        user.name = data['name']
        user.address = data['address']
        #user.phone = data['phone']
        user.email = data['email']
        user.username = data['username']
        user.password = data['password']
        user.role = data['role']
        return user

    def to_json(self) -> dict:
        data = {
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'role': self.role
        }
        return data