import contextlib
import importlib
import io
import math
import unittest
from unittest import mock

import requests


def load(module_name):
    # The practice files run example code on import: hide prints, answer input() and skip network calls
    with contextlib.redirect_stdout(io.StringIO()), \
         mock.patch("builtins.input", return_value="yes"), \
         mock.patch("requests.get", side_effect=requests.RequestException):
        return importlib.import_module(module_name)


def quiet():
    return contextlib.redirect_stdout(io.StringIO())


class TestBankAccount(unittest.TestCase):
    def test_deposit_and_interest(self):
        m = load("BankAccount")
        acc = m.Bankaccount("Test", 100)
        acc.deposit(50)
        with quiet():
            acc.add_interest()
        self.assertAlmostEqual(acc.balance, 153)


class TestMiniBank(unittest.TestCase):
    def setUp(self):
        self.bank = load("MiniBank").Bank("Test")
        self.bank.open_account("saving", "Marcoo")
        self.bank.open_account("checking", "Giulia")
        self.saving, self.checking = list(self.bank.accounts)

    def test_short_name_rejected(self):
        self.assertIn("valid name", self.bank.open_account("saving", "Bob"))
        self.assertEqual(len(self.bank.accounts), 2)

    def test_deposit_and_withdraw_limits(self):
        self.bank.deposit_money("saving", self.saving, "Marcoo", 100)
        self.assertEqual(self.bank.accounts[self.saving].balance, 100)
        self.assertIn("not eligible", self.bank.withdraw_money("saving", self.saving, "Marcoo", 150))
        self.bank.withdraw_money("checking", self.checking, "Giulia", 100)
        self.assertEqual(self.bank.accounts[self.checking].balance, -100)

    def test_transfer(self):
        self.bank.deposit_money("saving", self.saving, "Marcoo", 100)
        self.bank.transfer_money(40, self.saving, self.checking)
        self.assertEqual(self.bank.accounts[self.saving].balance, 60)
        self.assertEqual(self.bank.accounts[self.checking].balance, 40)


class TestMusicPlaylist(unittest.TestCase):
    def test_add_remove_no_duplicates(self):
        m = load("Music_Playlist")
        playlist = m.Playlist("Test")
        song = m.Song("Imagine", "John Lennon", 183)
        with quiet():
            playlist.add_song(song)
            playlist.add_song(song)
            self.assertEqual(len(playlist.playlists), 1)
            playlist.remove_song(song)
        self.assertEqual(playlist.playlists, [])


class TestPaymentSystem(unittest.TestCase):
    def setUp(self):
        self.m = load("PaymentSystem")

    def test_credit_card_adds_fee(self):
        card = self.m.CreditCard(1000)
        with quiet():
            card.pay_amount(100)
        self.assertEqual(card.credit_limit, 898)

    def test_paypal_insufficient_balance(self):
        paypal = self.m.Paypal(50)
        with quiet():
            paypal.pay_amount(100)
        self.assertEqual(paypal.balance, 50)

    def test_crypto_uses_rate(self):
        wallet = self.m.Crypto(1)
        with quiet(), mock.patch.object(self.m.Crypto, "get_crypto_rate", return_value=100):
            wallet.pay_amount(50)
        self.assertAlmostEqual(wallet.coin_amount, 0.5)


class TestRPGBattleArena(unittest.TestCase):
    def setUp(self):
        self.m = load("RPGBattleArena")

    def test_health_never_negative(self):
        hero = self.m.Characters("Hero", 10, 5)
        hero.take_damage(50)
        self.assertEqual(hero.health, 0)
        self.assertFalse(hero.is_alive())

    def test_warrior_shield_and_mage_spell(self):
        warrior = self.m.Warrior("Tank", 100, 5)
        mage = self.m.Mage("Wizard", 50, 10)
        mage.attacks(warrior)
        self.assertEqual(warrior.health, 75)
        self.assertEqual(mage.mana, 70)

    def test_battle_has_a_winner(self):
        a = self.m.Characters("A", 20, 10)
        b = self.m.Characters("B", 20, 3)
        with quiet():
            self.m.battle(a, b)
        self.assertTrue(a.is_alive())
        self.assertFalse(b.is_alive())


class TestRestaurant(unittest.TestCase):
    def test_order_flow(self):
        r = load("Restaurant").Restaurant("Test", 0.1)
        r.add_dish_to_menu("Pizza", 10)
        self.assertIn("already", r.add_dish_to_menu("Pizza", 12))
        with quiet(), mock.patch("builtins.input", return_value="yes"):
            table = r.open_order_for_table(0)
        self.assertIn(table, r.orders)
        r.add_dish_to_table("Pizza", table)
        self.assertIn("not currently available", r.add_dish_to_table("Sushi", table))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            r.tables_bill(table)
        self.assertIn("total : 11.00$", out.getvalue())


class TestSchoolPeople(unittest.TestCase):
    def test_raise_only_affects_one_teacher(self):
        m = load("SchoolPeople")
        a, b = m.Teacher("A", 30), m.Teacher("B", 40)
        a.raise_salary(500)
        self.assertEqual(a.Teacher_Salary, 3500)
        self.assertEqual(b.Teacher_Salary, 3000)

    def test_teaching_assistant_is_student_and_teacher(self):
        m = load("SchoolPeople")
        sam = m.teaching_assistant("Sam", 22)
        self.assertIsInstance(sam, m.Student)
        self.assertIsInstance(sam, m.Teacher)


class TestUniversitySystem(unittest.TestCase):
    def test_departments_and_students(self):
        m = load("UniversitySystem")
        uni = m.University("Test", 2000)
        uni.open_department("Maths")
        self.assertIn("already", uni.open_department("Maths"))
        dept = uni.get_department("Maths")
        dept.add_student("Ada")
        self.assertIn("already", dept.add_student("Ada"))
        uni.close_department("Maths")
        self.assertIsNone(uni.get_department("Maths"))

    def test_people_in_school_is_abstract(self):
        m = load("UniversitySystem")
        with self.assertRaises(TypeError):
            m.People_In_school("Nobody")


class TestAnimals(unittest.TestCase):
    def test_alive(self):
        m = load("animalsV2")
        self.assertTrue(m.Dog().alive)
        self.assertFalse(m.Car().alive)


class TestPhone(unittest.TestCase):
    def test_use_drains_battery(self):
        p = load("phone").phone("Apple", "iPhone", "80")
        p.use("10")
        self.assertEqual(p.battery, 60)


class TestShapeCalculator(unittest.TestCase):
    def setUp(self):
        self.m = load("shape_Calculator")

    def test_circle_from_radius_or_diameter(self):
        for circle in (self.m.Circle("c", radius=2), self.m.Circle("c", diameter=4)):
            circle.calculation_of_area()
            circle.calculation_of_perimeter()
            self.assertAlmostEqual(circle.area, 4 * math.pi)
            self.assertAlmostEqual(circle.perimeter, 4 * math.pi)

    def test_rectangle_and_square(self):
        rect = self.m.Rectangle("r", base=4, heights=3)
        square = self.m.Square("s", side=5)
        for shape in (rect, square):
            shape.calculation_of_area()
            shape.calculation_of_perimeter()
        self.assertEqual((rect.area, rect.perimeter), (12, 14))
        self.assertEqual((square.area, square.perimeter), (25, 20))


if __name__ == "__main__":
    unittest.main()
