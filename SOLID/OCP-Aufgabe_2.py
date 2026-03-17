'''
Aufgabe 2: Open/Closed Principle (OCP)

Ein Rabattsystem berechnet Nachlässe basierend auf dem Kundentyp (z. B. "Standard" und "Premium") mittels einer if-elif-Struktur innerhalb einer zentralen Methode.

Ihre Aufgabe: Strukturieren Sie das System so um, dass neue Rabattmodelle (z. B. "VIP") hinzugefügt werden können, ohne die bestehende Logik der Berechnungsklasse zu modifizieren. Nutzen Sie hierfür abstrakte Basisklassen (Python abc Modul) oder Vererbung.

Ziel: Die Software soll offen für Erweiterungen, aber geschlossen für Modifikationen sein.

Ausgangslage: Um einen neuen Kundentyp hinzuzufügen, müsste die Methode calculate_discount direkt verändert werden.

class DiscountCalculator:

    def calculate_discount(self, customer_type, price):

        if customer_type == "Standard":
            return price * 0.05

        elif customer_type == "Premium":
            return price * 0.10

        # Problem: Jede neue Rabattart erfordert ein neues 'elif'
        else:
            return 0

'''

from abc import ABC, abstractmethod

# 1) Abstrakte Basis
class DiscountStrategy(ABC):
    @abstractmethod
    def discount(self, price):
        pass


# 2) Konkrete Rabatte
class StandardDiscount(DiscountStrategy):
    def discount(self, price):
        return price * 0.05


class PremiumDiscount(DiscountStrategy):
    def discount(self, price):
        return price * 0.10


class VIPDiscount(DiscountStrategy):
    def discount(self, price):
        return price * 0.20


# 3) Calculator Umbau in Standard - Einfache Erweiterung durch neue Strategien
class DiscountCalculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate_discount(self, price):
        return self.strategy.discount(price)



calc_standard = DiscountCalculator(StandardDiscount())
print(calc_standard.calculate_discount(100))  # 5.0

calc_premium = DiscountCalculator(PremiumDiscount())
print(calc_premium.calculate_discount(100))   # 10.0

calc_vip = DiscountCalculator(VIPDiscount())
print(calc_vip.calculate_discount(100))       # 20.0

