import enum
from dataclasses import dataclass

__all__ = ("AvailableCurrency", "Currency", "rub", "usd")


class AvailableCurrency(enum.Enum):
    RUB = enum.auto()
    USD = enum.auto()


@dataclass(slots=True, frozen=True, eq=True, repr=True)
class Currency:
    code = AvailableCurrency


class RUB(Currency):
    currency: Currency = AvailableCurrency.RUB


class USD(Currency):
    currency: Currency = AvailableCurrency.USD


rub = RUB()
usd = USD()
