from multipledispatch import dispatch

class ZahlungsDispatcher:

    @dispatch(int)
    def zahlung(self, a, b=None):
        print("Buchung (int) =", a)

    @dispatch(float)
    def zahlung(self, a, b=None):
        print("Buchung (float) =", a)

    @dispatch(int, str)
    def zahlung(self, a, b=None):
        print("Bestätigung =", a, "Zahlungsmittel =", b)

    @dispatch(str, float)
    def zahlung(self, a, b=None):
        print("Quittung =", a, "Betrag =", b)

     # Optional: weitere Kombination (Erweiterbarkeit)
    @dispatch(str, int)
    def zahlung(self, a, b=None):
        print("Quittung =", a, "Betrag =", b)


z = ZahlungsDispatcher()

z.zahlung(100)
z.zahlung(49.95)
z.zahlung(120, "Kreditkarte")
z.zahlung("Namira", 19.99)

# Test der Erweiterung
z.zahlung("Tim", 30)