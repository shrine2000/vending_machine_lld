from src.states.vending_machine_state import VendingMachineState


class IdleState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self, amount):
        self.vending_machine.current_balnce += amount
        self.vending_machine.set_sate(self.vending_machine.selecting_product_state)
