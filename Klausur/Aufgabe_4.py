from abc import ABC, abstractmethod


# Interface PaymentProcessor (abstrakte Klasse)
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


# Konkrete Klasse CreditCardProcessor
class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount: float):
        print(f"Bezahlung von {amount:.1f}€ mit Kreditkarte")


# Externe Klasse PayPalAPI
class PayPalAPI:
    def send_payment(self, amount):
        print(f"PayPal: Sende Zahlung von {amount:.1f}€")


# Externe Klasse BitcoinAPI
class BitcoinAPI:
    def transfer(self, amount):
        print(f"Bitcoin: Überweise {amount:.2f} BTC")


# Adapter-Klasse PayPalAdapter
class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal_api: PayPalAPI):
        self.paypal_api = paypal_api

    def pay(self, amount: float):
        self.paypal_api.send_payment(amount)


# Adapter-Klasse BitcoinAdapter
class BitcoinAdapter(PaymentProcessor):
    def __init__(self, bitcoin_api: BitcoinAPI):
        self.bitcoin_api = bitcoin_api

    def pay(self, amount: float):
        btc_amount = amount / 30000
        self.bitcoin_api.transfer(btc_amount)
        print(f"(entspricht {amount:.2f} €)")


# Test-Skript
if __name__ == "__main__":
    kreditkarte = CreditCardProcessor()
    paypal = PayPalAdapter(PayPalAPI())
    bitcoin = BitcoinAdapter(BitcoinAPI())

    kreditkarte.pay(50.0)
    paypal.pay(75.0)
    bitcoin.pay(300.0)