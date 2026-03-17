# Aufgabe C:

class Mitarbeiter:

    def __init__(self, mitarbeiterID, name, position): # Konstruktor + Attribute aus Aufgabe
        self.__mitarbeiterID = mitarbeiterID
        self.__name = name
        self.__position = position
        self.__gehalt = 3000.0
        self.__erfahrungsjahre = 0
        
# Getter + Setter Methoden implementieren

    def get_mitarbeiterID(self):
        return self.__mitarbeiterID

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_gehalt(self):
        return self.__gehalt

    def get_erfahrungsjahre(self):
        return self.__erfahrungsjahre



    def set_mitarbeiterID(self, mitarbeiterID):
        self.__mitarbeiterID = mitarbeiterID

    def set_name(self, name):
        self.__name = name

    def set_position(self, position):
        self.__position = position

    def set_gehalt(self, gehalt):
        self.__gehalt = gehalt

    def set_erfahrungsjahre(self, erfahrungsjahre):
        self.__erfahrungsjahre = erfahrungsjahre


    # Methode zur Ausgabe aller Werte
    
    def werte_ausgeben(self):
        print("Mitarbeiter-ID:", self.__mitarbeiterID)
        print("Name:", self.__name)
        print("Position:", self.__position)
        print("Gehalt:", self.__gehalt)
        print("Erfahrungsjahre:", self.__erfahrungsjahre)

    # zwei weitere Methoden
    
    def befoerdern(self):
        print(self.__name, "wurde befördert.")

    def an_schulung_teilnehmen(self):
        print(self.__name, "nimmt an einer Schulung teil.")
        
        
# Aufgabe D: Anwendungsfälle im Hauptprogramm

def main():

    print("Mitarbeiter-System")

    # Mitarbeiter anlegen
    mitarbeiter = Mitarbeiter(101, "Max Mustermann", "Sachbearbeiter")

    print("\nMitarbeiter wurde angelegt:")
    mitarbeiter.werte_ausgeben()


    # Mitarbeiterdaten einsehen
    print("\nMitarbeiterdaten einsehen:")
    mitarbeiter.werte_ausgeben()


    # Mitarbeiterdaten ändern
    print("\nMitarbeiterdaten ändern")

    neues_gehalt = float(input("Neues Gehalt: "))
    neue_erfahrung = int(input("Neue Erfahrungsjahre: "))

    mitarbeiter.set_gehalt(neues_gehalt)
    mitarbeiter.set_erfahrungsjahre(neue_erfahrung)

    print("\nAktualisierte Mitarbeiterdaten:")
    mitarbeiter.werte_ausgeben()


    # Mitarbeiter befördern
    print("\nMitarbeiter befördern")
    mitarbeiter.befoerdern()


    # Schulung
    print("\nSchulung")
    mitarbeiter.an_schulung_teilnehmen()


if __name__ == "__main__":
    main()