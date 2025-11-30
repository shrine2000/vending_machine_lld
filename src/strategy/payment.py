import uuid
from abc import abstractmethod, ABC
from typing import Optional
from src.exceptions import PaymentException, InsufficientFundsException


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float, **kwargs) -> str:
        pass

    @abstractmethod
    def refund(self, amount: float, **kwargs) -> str:
        pass


class CashPayment(PaymentStrategy):
    def pay(self, amount: float, cash_given: float, **kwargs) -> str:
        if cash_given < amount:
            raise InsufficientFundsException(
                f"Insufficient funds. Required: ${amount:.2f}, Given: ${cash_given:.2f}"
            )
        transaction_id = f"cash_{uuid.uuid4().hex[:8]}_amt{amount:.2f}"
        return transaction_id

    def refund(self, amount: float, **kwargs) -> str:
        refund_id = f"cash_refund_{uuid.uuid4().hex[:8]}_amt{amount:.2f}"
        return refund_id


class CardPayment(PaymentStrategy):
    def pay(self, amount: float, card_number: str = "", **kwargs) -> str:
        transaction_id = f"card_{uuid.uuid4().hex[:8]}_amt{amount:.2f}"
        return transaction_id

    def refund(self, amount: float, **kwargs) -> str:
        refund_id = f"card_refund_{uuid.uuid4().hex[:8]}_amt{amount:.2f}"
        return refund_id
