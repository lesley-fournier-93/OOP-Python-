from functools import singledispatchmethod

class Verarbeite:
    @singledispatchmethod # Dekorator für die Methode
    def verarbeitet(self, x):
        print("Standardmeldung:", x)

    @verarbeitet.register
    def _(self, x: int):
        print("Int → Quadrat:", x * x)

    @verarbeitet.register
    def _(self, x: float):
        print("Float → Hälfte:", x / 2)

    @verarbeitet.register
    def _(self, x: str):
        print("String → Groß:", x.upper())

v = Verarbeite()
v.verarbeitet(6)        # int
v.verarbeitet(8.0)      # float
v.verarbeitet("hallo")  # str
v.verarbeitet([1, 2])   # list (Standard)