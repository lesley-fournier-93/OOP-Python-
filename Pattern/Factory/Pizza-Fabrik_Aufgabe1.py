from abc import ABC, abstractmethod


# abstrakte Basisklasse
class Pizza(ABC):

    @abstractmethod
    def zubereiten(self):
        pass

    @abstractmethod
    def backen(self):
        pass


# konkrete Pizza
class MargheritaPizza(Pizza):

    def zubereiten(self):
        print("Bereite Margherita mit Tomatensauce und Käse zu.")

    def backen(self):
        print("Backe Margherita bei 220°C für 10 Minuten.")


class SalamiPizza(Pizza):

    def zubereiten(self):
        print("Bereite Salami mit Tomatensauce, Käse und Salami zu.")

    def backen(self):
        print("Backe Salami bei 220°C für 12 Minuten.")


class HawaiiPizza(Pizza):

    def zubereiten(self):
        print("Bereite Hawaii mit Tomatensauce, Käse, Schinken und Ananas zu.")

    def backen(self):
        print("Backe Hawaii bei 220°C für 15 Minuten.")


# zusätzliche Pizza (für Erweiterung)
class VeganPizza(Pizza):

    def zubereiten(self):
        print("Bereite Vegan mit Tomatensauce, veganem Käse und Gemüse zu.")

    def backen(self):
        print("Backe Vegan bei 220°C für 11 Minuten.")


# Factory-Klasse
class PizzaFactory:

    pizza_typen = {
        "margherita": MargheritaPizza,
        "salami": SalamiPizza,
        "hawaii": HawaiiPizza
    }

    @staticmethod
    def create_pizza(pizza_type):

        if pizza_type in PizzaFactory.pizza_typen:
            return PizzaFactory.pizza_typen[pizza_type]()

        else:
            raise ValueError("Unbekannter Pizzatyp")


    @staticmethod
    def register(name, pizza_class):
        PizzaFactory.pizza_typen[name] = pizza_class



# Test / Anwendung
if __name__ == "__main__":

    factory = PizzaFactory()

    pizza1 = factory.create_pizza("margherita")
    pizza1.zubereiten()
    pizza1.backen()

    print()

    pizza2 = factory.create_pizza("salami")
    pizza2.zubereiten()
    pizza2.backen()

    print()

    pizza3 = factory.create_pizza("hawaii")
    pizza3.zubereiten()
    pizza3.backen()

    print()

    # neue Pizza registrieren
    PizzaFactory.register("vegan", VeganPizza)

    pizza4 = factory.create_pizza("vegan")
    pizza4.zubereiten()
    pizza4.backen()