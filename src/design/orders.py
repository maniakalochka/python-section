from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Order:
    """There is no need to describe anything here."""


class Discount(ABC):
    @abstractmethod
    def apply(self, amount: float) -> float:
        raise NotImplementedError("This method should be overridden by subclasses.")


@dataclass
class FixedDiscount(Discount):
    amount: float

    def apply(self, amount: float) -> float:
        return max(0, amount - self.amount)


@dataclass
class PercentageDiscount(Discount):
    percentage: float

    def apply(self, amount: float) -> float:
        return amount * (1 - self.percentage / 100.0)


@dataclass
class LoyaltyDiscount(Discount):
    loyalty_points: int

    def apply(self, amount: float) -> float:
        return max(0, amount - self.loyalty_points)


class DiscountManager:
    def __init__(self) -> None:
        self.discounts = []

    def add_discount(self, discount: Discount) -> None:
        self.discounts.append(discount)

    def apply_discounts(self, amount: float) -> float:
        for discount in self.discounts:
            amount = discount.apply(amount)
        return amount
