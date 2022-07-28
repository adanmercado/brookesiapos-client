from __future__ import annotations

from core.person import Person

class Customer(Person):
    def __init__(self) -> None:
        super(Customer, self).__init__()
    
    @staticmethod
    def from_json(data: dict) -> Customer:
        customer = Customer()
        customer.id = data['id']
        customer.name = data['name']
        customer.address = data['address']
        customer.phone = data['phone']
        customer.email = data['email']
        return customer

    def to_json(self) -> dict:
        data = super(Customer, self).to_json()
        return data