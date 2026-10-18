import io
import unittest
from contextlib import redirect_stdout

from MiniBank import Bank, GeneralAccount


def add_account(bank, account_type, owner, number, balance=0):
    """Put an account straight into the bank, so deposit/withdraw/transfer
    can be tested without depending on open_account."""
    cls = bank.Saving if account_type == "saving" else bank.Checking
    account = cls(owner, number)
    account.balance = balance
    bank.accounts[number] = account
    return account


class TestAccounts(unittest.TestCase):
    def test_general_account_starts_empty(self):
        acc = GeneralAccount("Lucaaa", 1)
        self.assertEqual(acc.owner, "Lucaaa")
        self.assertEqual(acc.accountnumber, 1)
        self.assertEqual(acc.balance, 0)

    def test_saving_has_zero_limit(self):
        acc = Bank.Saving("Lucaaa", 1)
        self.assertEqual(acc.balance, 0)
        self.assertEqual(acc.limit, 0)

    def test_checking_has_overdraft_limit(self):
        acc = Bank.Checking("Lucaaa", 1)
        self.assertEqual(acc.balance, 0)
        self.assertEqual(acc.limit, -100)


class TestOpenAccount(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Mini")

    def test_open_saving_account(self):
        self.bank.open_account("saving", "Marcoo")
        self.assertEqual(len(self.bank.accounts), 1)
        account = next(iter(self.bank.accounts.values()))
        self.assertIsInstance(account, Bank.Saving)
        self.assertEqual(account.owner, "Marcoo")

    def test_open_checking_account(self):
        self.bank.open_account("checking", "Marcoo")
        self.assertEqual(len(self.bank.accounts), 1)
        account = next(iter(self.bank.accounts.values()))
        self.assertIsInstance(account, Bank.Checking)

    def test_account_type_ignores_case_and_spaces(self):
        self.bank.open_account("  SaViNg ", "Marcoo")
        self.assertEqual(len(self.bank.accounts), 1)

    def test_unknown_account_type_is_rejected(self):
        result = self.bank.open_account("crypto", "Marcoo")
        self.assertIn("not available", result.lower())
        self.assertEqual(self.bank.accounts, {})

    def test_two_accounts_get_different_numbers(self):
        self.bank.open_account("saving", "Marcoo")
        self.bank.open_account("checking", "Giulia")
        self.assertEqual(len(self.bank.accounts), 2)

    def test_short_name_is_rejected_with_message(self):
        result = self.bank.open_account("saving", "Bob")
        self.assertIsNotNone(result)
        self.assertEqual(self.bank.accounts, {})

    def test_name_with_space_is_rejected_with_message(self):
        result = self.bank.open_account("saving", "Marco Rossi")
        self.assertIsNotNone(result)
        self.assertEqual(self.bank.accounts, {})

    def test_integer_name_is_rejected_without_crashing(self):
        result = self.bank.open_account("saving", 1234567)
        self.assertIsNotNone(result)
        self.assertEqual(self.bank.accounts, {})


class TestDeposit(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Mini")
        self.acc = add_account(self.bank, "saving", "Marcoo", 42)

    def test_deposit_increases_balance(self):
        result = self.bank.deposit_money("saving", 42, "Marcoo", 50)
        self.assertEqual(self.acc.balance, 50)
        self.assertIn("Successfully deposited", result)

    def test_deposit_accepts_string_amount(self):
        self.bank.deposit_money("saving", 42, "Marcoo", "25.5")
        self.assertEqual(self.acc.balance, 25.5)

    def test_deposit_invalid_account_type(self):
        result = self.bank.deposit_money("crypto", 42, "Marcoo", 50)
        self.assertEqual(result, "Please Enter A Valid Account Type")
        self.assertEqual(self.acc.balance, 0)

    def test_deposit_unknown_account_number(self):
        result = self.bank.deposit_money("saving", 999, "Marcoo", 50)
        self.assertIn("does not exist", result)

    def test_deposit_wrong_name(self):
        result = self.bank.deposit_money("saving", 42, "Giulia", 50)
        self.assertIn("does not match", result)
        self.assertEqual(self.acc.balance, 0)


class TestWithdraw(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Mini")
        self.saving = add_account(self.bank, "saving", "Marcoo", 1, balance=100)
        self.checking = add_account(self.bank, "checking", "Giulia", 2, balance=0)

    def test_withdraw_decreases_balance(self):
        result = self.bank.withdraw_money("saving", 1, "Marcoo", 40)
        self.assertEqual(self.saving.balance, 60)
        self.assertIn("Successfully withdrawn", result)

    def test_saving_can_withdraw_to_exactly_zero(self):
        self.bank.withdraw_money("saving", 1, "Marcoo", 100)
        self.assertEqual(self.saving.balance, 0)

    def test_saving_cannot_go_negative(self):
        result = self.bank.withdraw_money("saving", 1, "Marcoo", 101)
        self.assertIn("not eligible", result)
        self.assertEqual(self.saving.balance, 100)

    def test_checking_can_overdraw_to_limit(self):
        self.bank.withdraw_money("checking", 2, "Giulia", 100)
        self.assertEqual(self.checking.balance, -100)

    def test_checking_cannot_pass_limit(self):
        result = self.bank.withdraw_money("checking", 2, "Giulia", 101)
        self.assertIn("not eligible", result)
        self.assertEqual(self.checking.balance, 0)

    def test_withdraw_wrong_name(self):
        result = self.bank.withdraw_money("saving", 1, "Giulia", 10)
        self.assertIn("does not match", result)
        self.assertEqual(self.saving.balance, 100)

    def test_withdraw_unknown_account_number(self):
        result = self.bank.withdraw_money("saving", 999, "Marcoo", 10)
        self.assertIn("does not exist", result)


class TestFindAccount(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Mini")
        add_account(self.bank, "saving", "Marcoo", 7)

    def test_find_existing_account_greets_owner(self):
        result = self.bank.find_account_by_its_number(7)
        self.assertIn("Marcoo", result)

    def test_find_missing_account(self):
        result = self.bank.find_account_by_its_number(8)
        self.assertIn("not in the Database", result)


class TestTotalWorth(unittest.TestCase):
    def test_prints_each_account_and_total(self):
        bank = Bank("Mini")
        add_account(bank, "saving", "Marcoo", 1, balance=100)
        add_account(bank, "checking", "Giulia", 2, balance=50)
        out = io.StringIO()
        with redirect_stdout(out):
            bank.show_total_worth_of_bank()
        text = out.getvalue()
        self.assertIn("Marcoo 100", text)
        self.assertIn("Giulia 50", text)
        self.assertIn("Total Amount Held : 150", text)

    def test_empty_bank_total_is_zero(self):
        out = io.StringIO()
        with redirect_stdout(out):
            Bank("Mini").show_total_worth_of_bank()
        self.assertIn("Total Amount Held : 0", out.getvalue())


class TestTransfer(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Mini")
        self.sender = add_account(self.bank, "saving", "Marcoo", 1, balance=100)
        self.receiver = add_account(self.bank, "checking", "Giulia", 2, balance=0)

    def test_transfer_moves_money(self):
        result = self.bank.transfer_money(30, 1, 2)
        self.assertEqual(self.sender.balance, 70)
        self.assertEqual(self.receiver.balance, 30)
        self.assertEqual(result, "Successfully Transferred 30 from Marcoo to Giulia")

    def test_transfer_more_than_balance_is_refused(self):
        result = self.bank.transfer_money(150, 1, 2)
        self.assertIn("do not have", result)
        self.assertEqual(self.sender.balance, 100)
        self.assertEqual(self.receiver.balance, 0)

    def test_transfer_from_unknown_account_returns_message(self):
        result = self.bank.transfer_money(10, 999, 2)
        self.assertIsNotNone(result)
        self.assertEqual(self.receiver.balance, 0)

    def test_transfer_to_unknown_account_returns_message(self):
        result = self.bank.transfer_money(10, 1, 999)
        self.assertIsNotNone(result)
        self.assertEqual(self.sender.balance, 100)


if __name__ == "__main__":
    unittest.main()
