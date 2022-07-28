from __future__ import annotations

class Person:
    id: int
    name: str
    address : str
    phone: str
    email: str

    def __init__(self) -> None:
        self.id = 0
        self.name = ''
        self.address = ''
        self.phone = ''
        self.email = ''

    def to_json(self) -> dict:
        data = {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'email': self.email
        }
        return data