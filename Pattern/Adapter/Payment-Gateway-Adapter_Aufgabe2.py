class OldPaymentSystem:
    def pay(self, amount):
        return f"Alte Zahlung: von {amount} wurde durchgeführt"

class NewPaymentSystem:
    def make_payment(self, amount, currency):
        return f"Neue Zahlung: von {amount} {currency} wurde durchgeführt"


class PaymentAdapter:
    def __init__(self, new_payment_system):
        self.new_payment_system = new_payment_system

   
    def pay(self, amount):
        return self.new_payment_system.make_payment(amount, "EUR")



old_payment = OldPaymentSystem()
print(old_payment.pay(100))

new_payment = NewPaymentSystem()
adapter2 = PaymentAdapter(new_payment)
print(adapter2.pay(100))
