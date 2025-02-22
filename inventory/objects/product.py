import uuid

from robot.utils import is_number


class Product:
    def __init__(self, name: str, price: float = 0.0, count: int = 0):
        self.name = name
        self.count = count
        self.price = price

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if isinstance(value, int) and value >= 0:
            self._count = value
        else:
            raise ValueError("Count must be a non-negative integer.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if is_number(value) and value >= 0:
            self._price = value
        else:
            raise ValueError("Price must be a non-negative integer.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string value.")

    def __hash__(self):
        """
        Use name for hashing current product, to prevents situation for multiple products with same name
        :return: The name of the current product
        """
        return  hash(self.name)

    def __eq__(self, other):
        """
        Return if two elements are equals, based on the name.
        :param other: The second product to compare
        :return: True if both products have the same name, otherwise False
        """
        if isinstance(other, Product):
            return self.name == other.name
        return NotImplemented
