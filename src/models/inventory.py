from typing import Dict
from src.models.product import Product


class Inventory:
    def __init__(self):
        self._products: Dict[str, Product] = {}

    def add_product(self, product: Product):
        self._products[product.name] = product

    def get_product(self, product_name: str) -> Product:
        return self._products.get(product_name)

    def remove_product(self, product_name: str) -> bool:
        if product_name in self._products:
            del self._products[product_name]
            return True
        return False

    def get_all_products(self) -> Dict[str, Product]:
        return self._products.copy()

    def is_product_available(self, product_name: str) -> bool:
        product = self.get_product(product_name)
        return product is not None and product.is_available
