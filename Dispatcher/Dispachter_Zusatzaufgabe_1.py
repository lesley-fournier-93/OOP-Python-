from multipledispatch import dispatch

class Lagerverwaltung:

    @dispatch(str, int)
    def verarbeite(self, bestellung, menge):
        print("Bestellung bestätigt =", bestellung, "Menge =", menge)

    @dispatch(list, int)
    def verarbeite(self, bestellung, menge):
        print("Bestellübersicht =", bestellung, "Menge =", menge)

    @dispatch(dict, int)
    def verarbeite(self, bestellung, menge):
        print("Prüfe Lagerbestände (Grenze) =", menge)
        for produkt in bestellung:
            if bestellung[produkt] < menge:
                print("WARNUNG: niedriger Bestand =", produkt, bestellung[produkt])


l = Lagerverwaltung()

l.verarbeite("Tastatur", 3)
l.verarbeite(["Maus", "Monitor"], 2)
l.verarbeite({"Laptop": 5, "Drucker": 1, "Papier": 20}, 3)