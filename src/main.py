import sys
import os

# Add project root to sys.path to allow running as script
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.vending_machine import VendingMachine
from src.strategy.payment import CashPayment, CardPayment
from src.exceptions import (
    InsufficientFundsException,
    ProductNotFoundException,
    ProductOutOfStockException,
)


def main():
    vending_machine = VendingMachine(payment_strategy=CashPayment())

    vending_machine.add_product("Soda", 1.50, 10)
    vending_machine.add_product("Chips", 1.00, 5)
    vending_machine.add_product("Candy", 0.75, 20)

    print("\n" + "=" * 50)
    print("=== Vending Machine Demo ===")
    print("=" * 50 + "\n")

    vending_machine.show_products()

    print("Scenario 1: Successful purchase with change")
    print("-" * 50)
    try:
        vending_machine.insert_money(2.00)
        vending_machine.select_product("Soda")
        vending_machine.dispense_product()
        vending_machine.return_change()
    except Exception as e:
        print(f"Error: {e}")
    print()

    print("Scenario 2: Restock product")
    print("-" * 50)
    try:
        vending_machine.restock_product("Chips", 10)
    except Exception as e:
        print(f"Error: {e}")
    print()

    print("Scenario 3: Insufficient balance")
    print("-" * 50)
    try:
        vending_machine.insert_money(0.50)
        vending_machine.select_product("Chips")
    except Exception as e:
        print(f"Error: {e}")
    print()

    print("Scenario 4: Add more money and complete purchase")
    print("-" * 50)
    try:
        vending_machine.insert_money(0.60)
        vending_machine.select_product("Chips")
        vending_machine.dispense_product()
        vending_machine.return_change()
    except Exception as e:
        print(f"Error: {e}")
    print()

    print("Scenario 5: Product not found")
    print("-" * 50)
    try:
        vending_machine.insert_money(1.00)
        vending_machine.select_product("NonExistent")
    except ProductNotFoundException as e:
        print(f"Expected error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    print()

    print("Scenario 6: Exact change purchase (no change returned)")
    print("-" * 50)
    try:
        vending_machine.insert_money(0.75)
        vending_machine.select_product("Candy")
        vending_machine.dispense_product()
        vending_machine.return_change()
    except Exception as e:
        print(f"Error: {e}")
    print()

    print("=" * 50)
    print("Demo completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
