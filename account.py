class Account:
    """
    A class definition defines a account object
    """
    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of a account object
        :param name: Person's name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to deposit amount to balance
        :param amount: Amount to be added to balance
        :return: True: worked, False: did not work
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Method to withdraw amount from balance
        :param amount: Amount to be subtracted from balance
        :return: True: worked, False: did not work
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Method to access the account balance
        :return: Current balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to access the account name
        :return: Account name
        """
        return self.__account_name
