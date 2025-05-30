from dataclasses import dataclass

from .currency import Currency
from .exceptions import NegativeValueException, NotComparisonException


@dataclass(frozen=True)
class Money:
    value: float
    currency: Currency

    def __add__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise NotComparisonException("Cannot add money with different currencies")
        return Money(value=self.value + other.value, currency=self.currency)

    def __sub__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise NotComparisonException(
                "Cannot subtract money with different currencies"
            )
        result_value = self.value - other.value
        if result_value < 0:
            raise NegativeValueException("Resulting money value cannot be negative")
        return Money(value=result_value, currency=self.currency)

    def __post_init__(self) -> None:
        if self.value < 0:
            raise NegativeValueException("Money value cannot be negative")


class Wallet:
    def __init__(self, money: Money) -> None:
        self.money = money

    @property
    def currencies(self):
        return [self.money.currency] if self.money.value > 0 else []

    def __getitem__(self, currency: Currency) -> Money:
        if self.money.currency == currency:
            return self.money
        return Money(value=0, currency=currency)

    def __delitem__(self, currency: Currency) -> None:
        if self.money.currency == currency:
            self.money = Money(value=0, currency=self.money.currency)

    def __len__(self) -> int:
        return 1 if self.money.value > 0 else 0
