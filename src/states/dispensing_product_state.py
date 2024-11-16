from src.states.vending_machine_state import VendingMachineState


class DispensingProductState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def dispense_product(self):
        product = self.vending_machine.selected_product
        if product and product.dispense():
            change = self.vending_machine.current_balance - product.price
            if change > 0:
                self.vending_machine.set_state(
                    self.vending_machine.returning_change_state
                )
            else:
                self.vending_machine.reset_transaction()
        else:
            self.vending_machine.reset_transaction()
