from dataclasses import dataclass


class NotEnoughProductsInInventory(Exception):
    pass


class Warehouse:
    def __init__(self):
        self._product_name_to_inventory: dict[str, int] = {}

    def add(self, product_name: str, quantity: int) -> None:
        if product_name not in self._product_name_to_inventory:
            self._product_name_to_inventory[product_name] = 0

        self._product_name_to_inventory[product_name] += quantity

    def remove(self, product_name: str, quantity: int) -> None:
        if self.get_inventory(product_name) < quantity:
            raise NotEnoughProductsInInventory()

        self._product_name_to_inventory[product_name] -= quantity

    def get_inventory(self, product_name: str) -> int:
        return self._product_name_to_inventory.get(product_name, 0)

    def has_inventory(self, product_name: str, quantity) -> bool:
        return self.get_inventory(product_name) >= quantity
