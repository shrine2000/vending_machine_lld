from src.models.product import Product
from src.states.vending_machine_state import VendingMachineState
from src.vending_machine import VendingMachine


class SelectingProductState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine: VendingMachine = vending_machine

    def select_product(self, product: Product):
        product = self.vending_machine.get_product(product_name=product)
        if product and product.is_available():
            if self.vending_machine.current_balance >= product.price:
                self.vending_machine.set_state(
                    self.vending_machine.dispensing_product_state
                )
            else:
                self.vending_machine.set_state(self.vending_machine.idle_state)
        else:
            print("Product is out of stock.")
            self.vending_machine.set_state(self.vending_machine.out_of_stock_state)
