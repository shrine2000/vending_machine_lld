from src.states.vending_machine_state import VendingMachineState
from src.exceptions import ProductOutOfStockException


class DispensingProductState(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def dispense_product(self):
        product = self.vending_machine.selected_product

        if not product:
            print("No product selected.")
            self.vending_machine.reset_transaction()
            return

        if not product.dispense():
            raise ProductOutOfStockException(
                f"Failed to dispense {product.name}. Product may be out of stock."
            )

        try:
            transaction_id = self.vending_machine.payment_strategy.pay(
                amount=product.price, cash_given=self.vending_machine.current_balance
            )
            print(f"Dispensing {product.name}...")
            print(f"Payment processed. Transaction ID: {transaction_id}")

            self.vending_machine.current_balance -= product.price
            change = self.vending_machine.current_balance

            if change > 0:
                print(f"Change to return: ${change:.2f}")
                self.vending_machine.set_state(
                    self.vending_machine.returning_change_state
                )
            else:
                self.vending_machine.reset_transaction()
        except Exception as e:
            product.quantity += 1
            print(f"Payment failed: {e}")
            self.vending_machine.reset_transaction()
