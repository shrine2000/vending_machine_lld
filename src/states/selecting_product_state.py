from src.states.vending_machine_state import VendingMachineState
from src.exceptions import (
    ProductNotFoundException,
    ProductOutOfStockException,
    InsufficientFundsException,
    InvalidStateException,
)


class SelectingProductState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self, amount: float):
        self.vending_machine.current_balance += amount
        print(
            f"Additional money inserted: ${amount:.2f}. Current balance: ${self.vending_machine.current_balance:.2f}"
        )

    def select_product(self, product_name: str):
        product = self.vending_machine.get_product(product_name)

        if not product:
            raise ProductNotFoundException(f"Product '{product_name}' not found.")

        if not product.is_available:
            print(f"Product '{product_name}' is out of stock.")
            self.vending_machine.set_state(self.vending_machine.out_of_stock_state)
            return

        if self.vending_machine.current_balance < product.price:
            required = product.price
            available = self.vending_machine.current_balance
            print(
                f"Insufficient balance. Required: ${required:.2f}, Available: ${available:.2f}"
            )
            return

        self.vending_machine.selected_product = product
        print(f"Product selected: {product.name} (${product.price:.2f})")
        self.vending_machine.set_state(self.vending_machine.dispensing_product_state)

    def dispense_product(self):
        raise InvalidStateException("Please select a product first")
