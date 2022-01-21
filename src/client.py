import json
from src.queries import Queries
from src.order import Order

class Client:
    def __init__(self, id, firstName, lastName, email):
        if type(id) is not int:
            raise ValueError("id is not int")
        if type(firstName) is not str or not firstName:
            raise ValueError("firstName is not string")
        if Client.find_client(id):
            raise ValueError("client with this id already exists")
        if type(email) is not str or not email:
            raise ValueError("email is not string")
        if type(lastName) is not str or not lastName:
            raise ValueError("lastName is not string")
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.orders = []
        self.email = email
        Client.clients.append(self)
    clients = []
    def add_order(self, id):
        if type(id) is not int:
            raise ValueError("id is not int")
        self.orders.append(Order(id, self.id))
        Queries.add_order(id, self.id)

    def delete_order(self, id):
        if type(id) is not int:
            raise ValueError("id is not int")
        self.orders.remove(Order.find_order(id))
        Order.delete_order(id)