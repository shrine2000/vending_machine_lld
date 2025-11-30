from src.models.product import Product


class Slot:
    def __init__(self, slot_id: str, product: Product = None, capacity: int = 10):
        self._slot_id = slot_id
        self._product = product
        self._capacity = capacity

    @property
    def slot_id(self):
        return self._slot_id

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value: Product):
        self._product = value

    @property
    def capacity(self):
        return self._capacity

    @property
    def is_empty(self):
        return self._product is None or not self._product.is_available

    @property
    def is_full(self):
        return self._product is not None and self._product.quantity >= self._capacity

    def can_dispense(self) -> bool:
        return self._product is not None and self._product.is_available

    def dispense(self) -> bool:
        if self.can_dispense():
            return self._product.dispense()
        return False

    def restock(self, quantity: int):
        if self._product:
            new_quantity = min(self._product.quantity + quantity, self._capacity)
            self._product.quantity = new_quantity
        else:
            raise ValueError("Cannot restock empty slot. Set product first.")
