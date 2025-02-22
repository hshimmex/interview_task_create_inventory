import pytest
from inventory.objects.product import Product


@pytest.mark.parametrize("products, expected_value",
                         [([Product("Laptop", 10000.5, 10),
                            Product("Mouse", 25)], 100005),
                          ([Product("Phone", 502, 25),
                            Product("Mouse", 25, 1)], 12575),
                          ([], 0)])
def test_inventory_price(simple_inventory, products, expected_value):
    inventory = simple_inventory
    for product in products: inventory.add_product(product)
    value = inventory.total_inventory_value()
    assert value == expected_value, \
        f'Inventory total value is not as expected. Expected value: {expected_value}, but the actual value is {value}'


@pytest.mark.parametrize("products, expected_price_after_delete",
                         [([Product("Mouse", 10.55, 1),
                            Product("Laptop", 10000.5, 10),
                            Product("Mouse", 0, 0)], 100005),
                          ( [Product("Mouse")],0)])
def test_delete_product(simple_inventory, products, expected_price_after_delete):
    inventory = simple_inventory
    tested_product = products[0].name
    for product in products: inventory.add_product(product)
    inventory.remove_product(tested_product)

    assert inventory.get_product(tested_product) is None, \
        f"The product with name {tested_product} shouldn't be found, but it is exist on products list"

    inventory_total_value = inventory.total_inventory_value()
    assert inventory_total_value == expected_price_after_delete, \
        (f"Price after deletion {tested_product} is not as expected. Expected {expected_price_after_delete} "
         f"but found {inventory_total_value}")








