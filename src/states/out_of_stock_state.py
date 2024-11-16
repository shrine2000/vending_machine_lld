from src.states.vending_machine_state import VendingMachineState


class OutOfStockState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def restock_product(self, product_name, quantity):
        product = self.vending_machine.get_product(product_name)
        if product:
            product.quantity += quantity
            self.vending_machine.set_state(self.vending_machine.idle_state)
