import decimal
from dataclasses import dataclass
from typing import Any, Self

from .currency import Currency
from .exceptions import NegativeValueException, NotComparisonException


@dataclass(frozen=True, slots=True)
class Money:
    value: decimal.Decimal
    currency: Currency

    def __add__(self, other: "Money") -> "Money":
        self.check_same_currency(other)
        return Money(value=self.value + other.value, currency=self.currency)

    def __sub__(self, other: "Money") -> "Money":
        self.check_same_currency(other)
        result_value = self.value - other.value
        if result_value < 0:
            raise NegativeValueException("Resulting money value cannot be negative")
        return Money(value=result_value, currency=self.currency)

    def check_same_currency(self, other: "Money") -> None:
        if self.currency != other.currency:
            raise NotComparisonException("Cannot compare money with different currencies")

    def __post_init__(self) -> None:
        if self.value < 0:
            raise NegativeValueException("Money value cannot be negative")


class Wallet:
    def __init__(self, *args: Money) -> None:
        self.__storage = {}
        self.add(*args)

    @property
    def currencies(self):
        return self.__storage.keys()

    def ensure_currency_match(self, key: Currency, value: Money):
        if key != value.currency:
            raise ValueError(f"Key currency {key} does not match money currency {value.currency}")

    def __getitem__(self, currency: Currency) -> Any:
        return self.__storage.setdefault(
            currency,
            Money(value=decimal.Decimal(0), currency=currency))

    def __setitem__(self, currency: Currency, money: Money) -> None:
        self.ensure_currency_match(currency, money)
        self.__storage[currency] = money

    def __delitem__(self, key) -> None:
        if key in self.__storage:
            del self.__storage[key]

    def __len__(self) -> int:
        return len(self.currencies)

    def __contains__(self, currency: Currency) -> bool:
        return currency in self.__storage and self.__storage[currency].value > 0

    def add(self, money: Money) -> Self:
        self[money.currency] += money
        return self

    def sub(self, money: Money) -> Self:
        res = self[money.currency] - money
        if res.value < 0:
            raise NegativeValueException("Cannot subtract more money than available in the wallet")
        self[money.currency] = res
        return self
