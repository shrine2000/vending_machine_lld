from src.states.vending_machine_state import VendingMachineState
from src.exceptions import ProductNotFoundException


class OutOfStockState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def restock_product(self, product_name: str, quantity: int):
        product = self.vending_machine.get_product(product_name)
        if product:
            product.quantity += quantity
            print(
                f"Restocked {product_name}: {quantity} units. Total: {product.quantity}"
            )
            self.vending_machine.set_state(self.vending_machine.idle_state)
        else:
            raise ProductNotFoundException(
                f"Product '{product_name}' not found in inventory."
            )
