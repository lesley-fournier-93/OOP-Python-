from abc import ABC, abstractmethod


class Fahrzeug(ABC):
    """Abstrakte Basisklasse für alle Fahrzeuge."""

    @abstractmethod
    def fahren(self):
        pass


class Auto(Fahrzeug):
    """
    Standard-Auto.
    Autos sollen nur über die FahrzeugFactory erzeugt werden.
    """

    VALID_FACTORY_ID = 1234

    def __init__(self, f_id=VALID_FACTORY_ID):
        # Prüfen, ob das Auto von der richtigen Factory erzeugt wurde
        if f_id != self.VALID_FACTORY_ID:
            raise RuntimeError(
                "Fehler beim Erzeugen eines Autos.\n"
                f"Die übergebene Factory-ID ({f_id}) ist ungültig.\n"
                f"Erwartet wird die ID {self.VALID_FACTORY_ID}.\n"
                "Hinweis: Erzeuge Autos über FahrzeugFactory.produce_fahrzeug()."
            )

        self.factory_id = f_id

    def fahren(self):
        print("Das Auto fährt.")


class ElektroAuto(Auto):
    """Spezialisiertes Auto mit Elektroantrieb."""

    def fahren(self):
        print("Das Elektroauto fährt lautlos.")


# Basis-Factory
class FahrzeugFactory:
    """
    Factory zum Erzeugen von Fahrzeugen.
    Standardmäßig wird ein normales Auto produziert.
    """

    FAHRZEUG_KLASSE = Auto
    FACTORY_ID = 1234

    @classmethod
    def produce_fahrzeug(cls):
        print(f"Fabrik nutzt Vorlage: {cls.FAHRZEUG_KLASSE.__name__}")
        return cls.FAHRZEUG_KLASSE(f_id=cls.FACTORY_ID)


# Spezialisierte Factory
class ElektroFactory(FahrzeugFactory):
    """Factory für Elektroautos."""
    FAHRZEUG_KLASSE = ElektroAuto


if __name__ == "__main__":
    car1 = FahrzeugFactory.produce_fahrzeug()
    car1.fahren()

    print("-" * 20)

    car2 = ElektroFactory.produce_fahrzeug()
    car2.fahren()