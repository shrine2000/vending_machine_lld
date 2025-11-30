from src.exceptions import InvalidStateException


class VendingMachineState:
    def insert_money(self, money):
        raise InvalidStateException("Invalid operation in current state")

    def select_product(self, product):
        raise InvalidStateException("Invalid operation in current state")

    def dispense_product(self):
        raise InvalidStateException("Invalid operation in current state")

    def return_change(self):
        raise InvalidStateException("Invalid operation in current state")

    def restock_product(self, product_name, quantity):
        raise InvalidStateException("Invalid operation in current state")

    def get_current_state(self):
        pass
