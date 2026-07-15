from enum import Enum

class TransactionType(str, Enum):
    INCOME = "INCOME",
    EXPENSE = "EXPENSE"


class PaymentMethod(str, Enum):
    CASH = "CASH",
    CARD = "CARD",
    BANK_TRANSFER = "BANK_TRANSFER"