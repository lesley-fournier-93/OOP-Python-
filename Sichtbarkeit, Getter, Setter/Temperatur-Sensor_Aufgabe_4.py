'''
Aufgabe 4: Temperatur-Sensor mit Property-Dekorator

Sie entwickeln eine Klasse „TemperaturSensor“, die einen Temperaturwert speichert.

a) Implementieren Sie ein privates Attribut zur Speicherung der Temperatur.

b) Verwenden Sie den @property-Dekorator, um einen kontrollierten Zugriff zu ermöglichen. Selbst recherchieren was ein @property-Dekorator ist.

c) Stellen Sie sicher, dass nur realistische Temperaturwerte (z. B. zwischen -100 und 200 Grad Celsius) gesetzt werden können.

d) Erläutern Sie die Vorteile von Properties gegenüber klassischen Getter- und Setter-Methoden.

'''

class TemperaturSensor:
    def __init__(self):
        # Privates Attribut zur Speicherung der Temperatur
        self.__temperatur = 0.0

    @property
    def temperatur(self):
        """Gibt die aktuelle Temperatur zurück."""
        return self.__temperatur

    @temperatur.setter
    def temperatur(self, wert):
        """
        Setzt die Temperatur nur, wenn sie im realistischen Bereich liegt
        (-100 bis 200 Grad Celsius).
        """
        if -100 <= wert <= 200:
            self.__temperatur = wert
        else:
            raise ValueError(
                "Temperatur muss zwischen -100 und 200 Grad Celsius liegen."
            )

s = TemperaturSensor()
s.temperatur = 25     # klappt
s.temperatur = 500    # ValueError
        
'''
d) Vorteile von Properties gegenüber klassischen Getter- und Setter-Methoden:

- Zugriff erfolgt wie bei einem normalen Attribut (sensor.temperatur)

- Keine separaten get_- und set_-Methoden nötig

- Validierung kann im Hintergrund erfolgen

- Nachträgliche Erweiterung möglich, ohne den Zugriffscode zu ändern

- Bessere Lesbarkeit und sauberere Kapselung

- Python-typischer, moderner Stil

'''