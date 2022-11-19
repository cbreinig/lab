class Account:
    """
    A class representing details for an Account object
    """

    def __init__(self, name) -> None:
        """
        Constructor to create initial state of an Account object.
        :param name: Account's name.
        :param __int__(): Account's balance.
        """
        self.account_name = char(name)
        self.account_balance.__int__()

    def deposit(self, amount):
        """
        Method to add a deposit amount to the account balance.
        :return: positive amount boolean
        """
        amount = float(amount)
        if self.amount > 0:
            Account.account_balance = self.account_balance.__int__() + amount
            return True
        else:
            return False

    def withdraw(self, amount):
        """
        Method to subtract a withdrawal amount to the account balance.
        :return: positive amount boolean
                """
        amount = float(amount)
        if amount > 0:
            Account.account_balance = self.account_balance.__int__() - amount
            return True
        else:
            return False

    """
    Getters - accessors, for object balance and name
    """

    def get_balance(self):
        return self.account_balance.__int__()

    def get_name(self):
        return self.account_name.name
