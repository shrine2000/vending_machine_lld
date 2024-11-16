class Product:
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity

    @property
    def is_available(self):
        return self._quantity > 0

    def dispense(self):
        if self.is_available:
            self._quantity -= 1
            return True
        return False
