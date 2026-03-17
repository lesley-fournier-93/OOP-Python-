# private, public, protected
# Grundsätzlich : Atrribute nicht public --> Public von außen änderbar z.B. Name, Gehalt (keine Kontrolle)
# Programmier = Kontrolle behalten!
# zum Anfang er public programmieren und dann privatisieren! --> zwischendurch ausprobieren ob es funktiniert!

class Mitarbeiter:
# als erstes immer Konstruktor
    def __init__(self,p_name,gehalt):
        #public
        self.name = p_name

        #private
        self.__name = p_name

        #protected
        self._abteilung = "IT"

        #private
        self.__gehalt = gehalt

    #Fachliche Mehthoden

    def zeige_info(self):
        print(f" {self.__name},{self.__name},{self._abteilung})")

    def __berechne_bonus(self):
        return self.__gehalt*0.1

    # Idee von Getter und Setter Methoden: protected und private Atrribute zu
    # Konsequenz: Für jedes Attribut 1 Setter und ein 1 Getter
    # Getter/Setter werden nicht in UML modelliert (würde Diagramme unübersichtlich machen)

    def getName(self): # Lese-Methode, diese Methode ist public
        return self.__name

    def setName(self, wert): # Schreiben
        '''self.__name = wert '''

        #Hier kann man eine Zugriffslogik implementieren (Kontrolle ausüben)

        if wert == "Hallo":
            print("Fehlermeldung")
        else:
            self.__name = wert #Zuweisung

   

m = Mitarbeiter("Schmidt",5000)

print(m.name)
print(m._abteilung) # !!!!!!!!!!!!!!!

#print(m.__gehalt)
print(m._Mitarbeiter__gehalt) # ???!!!!!!!!!!!!!!!!!

print(m.getName())
m.setName("Meyer")
print(m.getName())

# Schmidt bleibt und es kann nicht in Meyer geändert werden! (Kontrolle ausüben)
