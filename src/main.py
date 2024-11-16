from src.vending_machine import VendingMachine

if __name__ == "__main__":
    vending_machine = VendingMachine()

    vending_machine.add_product("Soda", 1.50, 10)
    vending_machine.add_product("Chips", 1.00, 5)

    vending_machine.insert_money(2.00)
    vending_machine.select_product("Soda")
    vending_machine.dispense_product()

    vending_machine.restock_product("Chips", 10)
