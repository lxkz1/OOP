from abc import ABC , abstractmethod
import requests

class Payment_Method(ABC):
    @abstractmethod
    def pay_amount(self,amount):
        pass

    @abstractmethod
    def describe(self):
        pass

class CreditCard(Payment_Method):

    fee = 2

    def __init__(self, credit_limit):
        self.credit_limit = credit_limit

    def pay_amount(self,amount):
        amount_after_fee = (float(amount)/100) * float(CreditCard.fee)
        if  (float(amount) + amount_after_fee) > float(self.credit_limit):
            print("Credit limit reached")
        else:
            amount += amount_after_fee
            self.credit_limit -= amount
            print(f"Successfully deducted {amount} from your credit limit")

    def describe(self):
        print(f"Credit Card , credit limit {self.credit_limit}")

class Paypal(Payment_Method):
    def __init__(self,balance):
        self.balance = balance

    def pay_amount(self,amount):
        if float(amount) > float(self.balance):
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Successfully deducted {amount} from your balance")

    def describe(self):
        print(f"Paypal Account , Balance {self.balance}")


class Crypto(Payment_Method):

    FALLBACK_RATE = 50000
    stored_crypto_rate = 0

    def get_crypto_rate(self,coin="bitcoin"):
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": coin, "vs_currencies": "eur"}
        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            Crypto.stored_crypto_rate = response.json()[coin]["eur"]
            return Crypto.stored_crypto_rate
        except (requests.RequestException, KeyError, ValueError):
            print("Couldn't get the live rate, using the fixed one.")
            return Crypto.FALLBACK_RATE

    def __init__(self,coin_amount = 0):
        self.coin_amount = coin_amount

    def pay_amount(self,amount):
        coin = self.get_crypto_rate()
        coins = float(amount) / coin
        if self.coin_amount < coins:
            print("Insufficient Coin balance")
        else:
            self.coin_amount -= coins
            print(f"Successfully deducted {coins} from account")

    def describe(self):
        print(f"coin account, {self.coin_amount} coins")


card = CreditCard(1000)
paypal = Paypal(200)
wallet = Crypto(0.01)
card.pay_amount(100)
paypal.pay_amount(50)
wallet.pay_amount(100)
card.pay_amount(5000)
paypal.pay_amount(500)
wallet.pay_amount(1000000)
methods = [card, paypal, wallet]
for m in methods:
    m.pay_amount(20)
    m.describe()
