from src.states.vending_machine_state import VendingMachineState


class ReturningChangeState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def return_change(self):
        change = (
            self.vending_machine.current_balance
            - self.vending_machine.selected_product.price
        )
        self.vending_machine.reset_transaction()
