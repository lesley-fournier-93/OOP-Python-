from abc import ABC, abstractmethod


# Subject (Stock)
class Stock:
    def __init__(self, name, price):
        self._observers = []
        self.name = name
        self._price = price

    def add_observer(self, observer):  # Anmeldung
        self._observers.append(observer)

    def remove_observer(self, observer):  # Abmeldung
        self._observers.remove(observer)

    def notify_observers(self):  # alle Observer werden benachrichtigt
        for observer in self._observers:
            observer.update(self._price)

    # Wenn sich der Kurs ändert, werden alle Observer benachrichtigt
    def set_price(self, price):
        self._price = price
        self.notify_observers()


# Observer Interface
class Observer(ABC):  # Beobachter
    @abstractmethod
    def update(self, price:float):
        pass


# Concrete Observer: Email Alert
class EmailAlert(Observer):
    def update(self, price):
        print(f"Email Alert: Neuer Kurs von Tesla = {price}€")


# Concrete Observer: Mobile App
class MobileApp(Observer):
    def update(self, price):
        print(f"Mobile App: Tesla steht jetzt bei {price}€")


# Concrete Observer: Trading Bot
class TradingBot(Observer):
    def update(self, price):
        if price < 100:
            entscheidung = "Kaufen"
        else:
            entscheidung = "Halten"
        print(f"Trading Bot: Kurs von Tesla = {price}€, Entscheidung: {entscheidung}")


if __name__ == "__main__":

    # Erstelle ein Stock-Objekt
    stock = Stock("Tesla", 100)

    # Observer
    email_alert = EmailAlert()
    mobile_app = MobileApp()
    trading_bot = TradingBot()

    # Registriere mehrere Observer
    stock.add_observer(email_alert)
    stock.add_observer(mobile_app)
    stock.add_observer(trading_bot)

    # Simuliere Kursänderungen
    stock.set_price(105)
    stock.set_price(95)