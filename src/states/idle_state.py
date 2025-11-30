from src.states.vending_machine_state import VendingMachineState
from src.exceptions import ProductNotFoundException, InvalidStateException


class IdleState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self, amount: float):
        self.vending_machine.current_balance += amount
        self.vending_machine.set_state(self.vending_machine.selecting_product_state)
        print(
            f"Money inserted: ${amount:.2f}. Current balance: ${self.vending_machine.current_balance:.2f}"
        )

    def restock_product(self, product_name: str, quantity: int):
        product = self.vending_machine.get_product(product_name)
        if product:
            product.quantity += quantity
            print(
                f"Restocked {product_name}: {quantity} units. Total: {product.quantity}"
            )
        else:
            raise ProductNotFoundException(
                f"Product '{product_name}' not found in inventory."
            )

    def select_product(self, product_name: str):
        raise InvalidStateException("Please insert money first")

    def return_change(self):
        print("No money to return.")
