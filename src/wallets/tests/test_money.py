import math

import pytest

from src.wallets.currency import Currency
from src.wallets.exceptions import NegativeValueException, NotComparisonException
from src.wallets.money import Money, Wallet


class TestMoney:
    @pytest.fixture
    def money1(self):
        return Money(value=1, currency=Currency.rub)

    @pytest.fixture
    def money2(self):
        return Money(value=2, currency=Currency.rub)

    @pytest.fixture
    def money3(self):
        return Money(value=3, currency=Currency.rub)

    def test_add(self, money1, money2, money3):
        assert money1 + money2 == money3

    def test_sub(self, money1, money2, money3):
        assert money3 - money2 == money1

    def test_other_currency(self, money1, money2, money3):
        with pytest.raises(NotComparisonException):
            Money(value=1, currency=Currency.rub) + Money(
                value=1, currency=Currency.usd
            )


class TestWallet:
    @pytest.fixture
    def money(self):
        return Money(value=500, currency=Currency.rub)

    @pytest.fixture
    def wallet(self, money):
        return Wallet(money)

    def test_get__exists(self, wallet, money):
        assert wallet[Currency.rub] == money

    def test_get__empty(self, wallet):
        assert wallet[Currency.usd] == Money(value=0, currency=Currency.usd)

    def test_del__exists(self, wallet):
        del wallet[Currency.rub]
        assert Currency.rub not in wallet.currencies

    def test_del__empty(self, wallet):
        del wallet[Currency.usd]
        assert Currency.usd not in wallet.currencies

    def test_len_currencies(self, wallet):
        assert len(wallet) == 1

    def test_contains(self, wallet):
        assert Currency.rub in wallet
        assert Currency.usd not in wallet

    def test_add(self, wallet):
        wallet.add(Money(value=100, currency=Currency.rub)).add(
            Money(value=200, currency=Currency.rub)
        )
        assert wallet[Currency.rub] == Money(value=800, currency=Currency.rub)

    def test_sub(self, wallet):
        wallet.sub(Money(value=100, currency=Currency.rub)).sub(
            Money(value=200, currency=Currency.rub)
        )
        assert wallet[Currency.rub] == Money(value=200, currency=Currency.rub)

    def test_sub__negative(self, wallet):
        with pytest.raises(NegativeValueException):
            wallet.sub(Money(value=math.inf, currency=Currency.rub))
