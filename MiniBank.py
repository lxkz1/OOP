import random

class GeneralAccount:
    def __init__(self,owner, accountnumber,) -> None:
        self.owner = owner
        self.accountnumber = accountnumber
        self.balance = 0

class Bank:
    class Saving(GeneralAccount):
        def __init__(self,owner, accountnumber) -> None:
            super().__init__(owner,accountnumber)
            self.balance = 0
            self.limit = 0
    class Checking(GeneralAccount):
        limit = -100
        def __init__(self,owner,accountnumber) -> None:
            super().__init__(owner,accountnumber)
            self.balance = 0
            self.limit = -100
    def __init__(self,name):
        self.name = name
        self.accounts = {}

    def open_account(self, account_type, owner_name):
        if isinstance(owner_name, int) or len(owner_name) <= 5 or " " in str(owner_name):
            return f"Please Re-Enter a valid name for the account which contain 5 or more letters no numbers and no spaces"
        else:
            while True:
                new_account_number = random.randint(1,10000000)
                if new_account_number != self.accounts:
                    break
                else:
                    continue
            account_types = str(account_type).strip().lower()
            if account_types not in ["saving", "checking"]:
                return f"The Account Type You Entered Is Not Available At {self.name} Bank"
            elif account_types == "saving":
                a = self.Saving(owner_name,new_account_number)
                self.accounts[new_account_number] = a
            elif account_types == "checking":
                a = self.Checking(owner_name,new_account_number)
                self.accounts[new_account_number] = a

    def deposit_money(self,account_type,account_number,account_name,amount_to_deposit):
        if account_type not in ["saving", "checking"]:
            return f"Please Enter A Valid Account Type"
        else:
            if account_number not in self.accounts:
                return f"Your account does not exist in our database"
            else:
                account = self.accounts[account_number]
                if str(account_name) != account.owner:
                    return f"the name hav eprovided does not match the account number"
                else:
                    account.balance += float(amount_to_deposit)
                    return f"Successfully deposited {amount_to_deposit:.2f}"

    def withdraw_money(self,account_type,account_number,account_name,amount_to_withdraw):
        if account_type not in ["saving", "checking"]:
            return f"Please Enter A Valid Account Type"
        else:
            if account_number not in self.accounts:
                return f"Your account does not exist in our database"
            else:
                account = self.accounts[account_number]
                if str(account_name) != account.owner:
                    return f"the name hav eprovided does not match the account number"
                else:
                    if (float(account.balance) - float(amount_to_withdraw)) < account.limit:
                        return f"You account is not eligible for the amount you want to withdraw since is surpasses the account limit of {account.limit}"
                    else:
                        account.balance -= float(amount_to_withdraw)
                        return f"Successfully withdrawn {amount_to_withdraw} from your account"


    def find_account_by_its_number(self, account_number):
        if account_number in self.accounts:
            a = self.accounts[account_number]
            return f"Welcome back {a.owner} its a pleasure to have you back at our bank"
        else:
            return f"You're account number is not in the Database"

    def show_total_worth_of_bank(self):
        total = 0
        for account in self.accounts:
            accounts = self.accounts[account]
            print(accounts.owner , accounts.balance)
        for account in self.accounts:
            accounts = self.accounts[account]
            total += accounts.balance
        print(f"Total Amount Held : {total}")

    def transfer_money(self, amount, account_number,ndaccountnumber):
        if account_number not in self.accounts:
            return f"The account you want to send money from does not exist in our database"
        elif ndaccountnumber not in self.accounts:
            return f"The account you want to send money to does not exist in our database"
        else:
            a = self.accounts[account_number]
            b = self.accounts[ndaccountnumber]
            if amount > a.balance:
                return f"You do not have {amount} in your current account balance"
            else:
                b.balance += amount
                a.balance -= amount
                return f"Successfully Transferred {amount} from {a.owner} to {b.owner}"



















