from __future__ import annotations

from .person import Person

class User(Person):
    username: str
    password: str
    role: int

    def __init__(self) -> None:
        super(User, self).__init__()
        self.username = ''
        self.password = ''
        self.role = 0
    
    @staticmethod
    def from_json(data: dict) -> User:
        user = User()
        user.id = data['id']
        user.name = data['name']
        user.address = data['address']
        user.phone = data['phone']
        user.email = data['email']
        user.username = data['username']
        user.password = data['password']
        user.role = data['role']
        return user

    def to_json(self) -> dict:
        data = super(User, self).to_json()
        data['username'] = self.username
        data['password'] = self.password
        data['role'] = self.role
        return data