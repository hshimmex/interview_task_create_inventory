from inventory.objects.product import Product

class Inventory:

    def __init__(self, name):
        self._name = name
        self._products = set()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string value.")


    def add_product(self, product: Product):
        """
        Add some product to products list
        :param product: The product to add to the list
        :return: None
        """
        self._products.add(product)

    def get_product(self, name: str) -> Product | None:
        """
        Retrieve specific product from the products list, and return it.
        :param name: The name of the returned product
        :return: the product with the given name if found, None if no product is found.
        """
        for product in self._products:
            if product.name == name:
                return product
        return None

    def remove_product(self, name: str):
        """
        Remove the specific product from the inventory list
        :param name: Which products to remove
        :return: None
        """
        product = self.get_product(name)
        self._products.remove(product)

    def total_inventory_value(self) -> float:
        """
        Go over all products and return the total value of the inventory.
        :return: Return the total value of the inventory. If there is no product in the list, return 0.
        """
        return sum(product.price * product.count for product in self._products if product.count > 0 and product.price > 0)
