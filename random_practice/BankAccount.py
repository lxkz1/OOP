class Bankaccount:

    bank_name = "PyBank"
    interest_rate = 0.02
    account_count = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        Bankaccount.account_count += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount >= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Funds")

    def add_interest(self):
        interestearned = self.balance * Bankaccount.interest_rate
        self.balance += interestearned
        print(f"You Earned a total interest of {interestearned}")

    def describe(self):
        print(f"{self.owner} at {Bankaccount.bank_name} - balance: {self.balance}")


Owner1 = Bankaccount("Luca", 100)
Owner2 = Bankaccount("Lucas", 101)
Owner3 = Bankaccount("lxkz", 102)


Owner1.add_interest()
print(f"Your Have a Total Balance of {Owner1.balance}")
Owner1.describe()

Owner2.add_interest()
print(f"Your Have a Total Balance of {Owner2.balance}")
Owner2.describe()

Owner3.add_interest()
print(f"Your Have a Total Balance of {Owner3.balance}")
Owner3.describe()