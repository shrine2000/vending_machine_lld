class VendingMachineException(Exception):
    pass


class InsufficientFundsException(VendingMachineException):
    pass


class ProductNotFoundException(VendingMachineException):
    pass


class ProductOutOfStockException(VendingMachineException):
    pass


class InvalidStateException(VendingMachineException):
    pass


class PaymentException(VendingMachineException):
    pass
