'''
Praxisaufgaben: Dependency Injection in Python
Die folgenden Aufgaben behandeln das Konzept der Dependency Injection (DI) in Python. 
Die Aufgaben sind praxisnah. Bearbeiten Sie die Aufgaben strukturiert und nachvollziehbar.
Aufgabe 1: Kaffeemaschine mit austauschbarem Heizsystem
Sie entwickeln die Software für eine Kaffeemaschine. Die Klasse 'CoffeeMachine' benötigt 
ein Heizsystem, um Wasser zu erhitzen. Aktuell ist die Klasse direkt von einer konkreten 
Klasse 'ElectricHeater' abhängig.
a) Implementieren Sie eine Lösung ohne Dependency Injection.
b) Refaktorieren Sie die Lösung so, dass das Heizsystem per Konstruktor injiziert wird.
c) Implementieren Sie zusätzlich eine Klasse 'GasHeater' und zeigen Sie, wie die 
Kaffeemaschine ohne Codeänderung mit diesem neuen Heizsystem betrieben werden kann.
Hinweis: Die Kaffeemaschine soll lediglich die Methode 'heat()' des Heizsystems aufrufen. 
Ob elektrisch oder gasbetrieben erhitzt wird, soll der Maschine egal sein.

'''

# a) Lösung ohne Dependency Injection --> CoffeeMachine direkt von ElectricHeater abhängig = harte Kopplung

class ElectricHeater:
    def heat(self):
        print("Heating water with electricity...")


class CoffeeMachine:
    def __init__(self):
        # Harte Abhängigkeit!
        self.heater = ElectricHeater()

    def make_coffee(self):
        self.heater.heat()
        print("Brewing coffee...")

machine = CoffeeMachine()
machine.make_coffee()

# Problem: CoffeeMachine erstellt selbst Heiysystem
# wenn wir eine anderes Heizsystem wollen (z.B. Gas), müssen wir Klassen ändern
# dadurch schlechte Testbarkeit
# hohe Kopplung


# b) Refaktorierung mit Dependency Injection --> Heizsystem wird von außen übergeben - Kaffeemaschine braucht nur heat()-Methode

class ElectricHeater:
    def heat(self):
        print("Heating water with electricity...")

# c) Neues Heizsystem: GasHeater

class GasHeater:
    def heat(self):
        print("Heating water with gas flame...")


class CoffeeMachine:
    def __init__(self, heater):
        self.heater = heater

    def make_coffee(self):
        self.heater.heat()
        print("Brewing coffee...")

electric_heater = ElectricHeater()
machine = CoffeeMachine(electric_heater)
machine.make_coffee()

gas_heater = GasHeater()
machine = CoffeeMachine(gas_heater)
machine.make_coffee()

# welches Heizsystem ist jetzt völlig egal CoffeeMaschine bleibt unverändert!