import os


class Limit:
    limit: int

    @classmethod
    def set_limit(cls, x: int):
        cls.limit = x

    @classmethod
    def get_limit(cls):
        return cls.limit
class Product:
    count = 0

    def __init__(self, name):
        if Product.count < Limit.get_limit():
            Product.count = Product.count + 1
            self.name = name
        else:
            raise UserLimitExceeded(f"Product {name} cannot be created. Maximum {Limit.get_limit()} products allowed")

    def __del__(self):
        if Product.count > 0:
            Product.count -= 1


class UserLimitExceeded(Exception):
    def __init__(self, message):
        self.message = message