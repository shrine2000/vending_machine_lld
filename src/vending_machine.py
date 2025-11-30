from typing import Optional
from src.models.product import Product
from src.models.inventory import Inventory
from src.strategy.payment import PaymentStrategy, CashPayment
from src.states.idle_state import IdleState
from src.states.selecting_product_state import SelectingProductState
from src.states.dispensing_product_state import DispensingProductState
from src.states.returning_change_state import ReturningChangeState
from src.states.out_of_stock_state import OutOfStockState
from src.states.vending_machine_state import VendingMachineState


class VendingMachine:
    def __init__(self, payment_strategy: Optional[PaymentStrategy] = None):
        self.inventory = Inventory()
        self.current_balance = 0.0
        self.selected_product: Optional[Product] = None
        self.payment_strategy = payment_strategy or CashPayment()

        self.idle_state = IdleState(self)
        self.selecting_product_state = SelectingProductState(self)
        self.dispensing_product_state = DispensingProductState(self)
        self.returning_change_state = ReturningChangeState(self)
        self.out_of_stock_state = OutOfStockState(self)

        self.current_state: VendingMachineState = self.idle_state

    def set_state(self, state: VendingMachineState):
        self.current_state = state

    def insert_money(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.current_state.insert_money(amount)

    def select_product(self, product_name: str):
        self.current_state.select_product(product_name)

    def dispense_product(self):
        self.current_state.dispense_product()

    def return_change(self):
        self.current_state.return_change()

    def restock_product(self, product_name: str, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.current_state.restock_product(product_name, quantity)

    def get_product(self, product_name: str) -> Optional[Product]:
        return self.inventory.get_product(product_name)

    def add_product(self, product_name: str, price: float, quantity: int):
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        product = Product(product_name, price, quantity)
        self.inventory.add_product(product)

    def reset_transaction(self):
        print("Transaction completed.")
        self.current_balance = 0.0
        self.selected_product = None
        self.current_state = self.idle_state

    def get_current_balance(self) -> float:
        return self.current_balance

    def get_state_name(self) -> str:
        return self.current_state.__class__.__name__

    def show_products(self):
        print("\nAvailable Products:")
        for name, product in self.inventory.get_all_products().items():
            if product.is_available:
                print(f"- {name}: ${product.price:.2f} ({product.quantity} available)")
            else:
                print(f"- {name}: Out of Stock")
        print()
