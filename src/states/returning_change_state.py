from src.states.vending_machine_state import VendingMachineState


class ReturningChangeState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def return_change(self):
        change = self.vending_machine.current_balance

        if change > 0:
            refund_id = self.vending_machine.payment_strategy.refund(amount=change)
            print(f"Returning change: ${change:.2f}")
            print(f"Refund processed. Transaction ID: {refund_id}")

        self.vending_machine.reset_transaction()
