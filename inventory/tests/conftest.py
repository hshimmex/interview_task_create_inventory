import pytest
from inventory.objects.inventory import Inventory


@pytest.fixture
def simple_inventory():
    inventory = Inventory("tested_inventory")
    return inventory

