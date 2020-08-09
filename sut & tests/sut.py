from decimal import Decimal


class Account:
    def __init__(self, name, start_balance):
        self.set_name(name)
        self.set_balance(start_balance)

    def set_name(self, name):
        self.__name = str(name)

    def set_balance(self, balance):
        self.__balance = Decimal(balance)

    def balance(self):
        return self.__balance

    def name(self):
        return self.__name

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def transfer_to(self, account, amount):
        if not isinstance(account, Account):
            raise TypeError("account must be another Account")

        self.withdraw(amount)
        account.deposit(amount)

    def transfer_from(self, account, amount):
        if not isinstance(account, Account):
            raise TypeError("account must be another Account")

        account.withdraw(amount)
        self.deposit(amount)

    def __str__(self):
        return "Account({}, {})".format(self.__name, self.__balance)


if __name__ == "__main__":
    a = Account("A", 1000)
    b = Account("B", 5000)

    print(a)
    print(b)

    a.transfer_to(b, 500)

    print(a)
    print(b)

    a.transfer_from(b, 1000)

    print(a)
    print(b)
