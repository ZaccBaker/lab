import pytest
from account import *


class Test:
    def setup_method(self):
        self.p1 = Account('John')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'John'
        assert self.p1.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(10) is True
        assert self.p1.get_balance() == 10
        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == 10
        assert self.p1.deposit(-1) is False
        assert self.p1.get_balance() == 10
        assert self.p1.deposit(10.05) is True
        assert self.p1.get_balance() == pytest.approx(20.05, abs=0.01)

    def test_withdraw(self):
        self.p1.deposit(50)
        assert self.p1.withdraw(10) is True
        assert self.p1.get_balance() == 40
        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == 40
        assert self.p1.withdraw(-1) is False
        assert self.p1.get_balance() == 40
        assert self.p1.withdraw(10.05) is True
        assert self.p1.get_balance() == pytest.approx(29.95, abs=0.01)
        assert self.p1.withdraw(1000) is False
        assert self.p1.get_balance() == pytest.approx(29.95, abs=0.01)


if __name__ == '__main__':
    pytest.main()
