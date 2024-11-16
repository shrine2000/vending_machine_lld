from src.models.product import Product
from src.states.idle_state import IdleState
from src.states.selecting_product_state import SelectingProductState
from src.states.dispensing_product_state import Dis


class VendingMachine:
    def __init__(self):
        self.products = {}
        self.current_balance = 0
        self.idle_state = IdleState(self)
        self.selecting_product_state = SelectingProductState(self)
        self.dispensing_product_state = DispensingProductState(self)
        self.returning_change_state = ReturningChangeState(self)
        self.out_of_stock_state = OutOfStockState(self)
        self.current_state = self.idle_state

    def insert_money(self, amount):
        self.current_state.insert_money(amount)

    def select_product(self, product_name):
        self.current_state.select_product(product_name)

    def dispense_product(self):
        self.current_state.dispense_product()

    def return_change(self):
        self.current_state.return_change()

    def restock_product(self, product_name, quantity):
        self.current_state.restock_product(product_name, quantity)

    def get_product(self, product_name):
        return self.products.get(product_name)

    def add_product(self, product_name, price, quantity):
        self.products[product_name] = Product(product_name, price, quantity)

    def reset_transaction(self):
        print("Transaction completed.")
        self.current_balance = 0
        self.selected_product = None
        self.current_state = self.idle_state
