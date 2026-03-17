# private, public, protected
# Grundsätzlich: Attribute nicht public


class Mitarbeiter:
    ''' ljejhfjkl<dfjäkldjfd'''



# als erste erste Konstruktor
    def __init__(self,p_name,gehalt): #Konstruktor
        #private
        self.__name = p_name

        #protected
        self._abteilung = "IT"

        #private
        self.__gehalt = gehalt

#Fachlichen Methoden

    def zeige_ifo(self):
        print(f" {self.name},{self.name},{self._abteilung})")


    def __berechne_bonus(self):
        return self.__gehalt * 0.1




    # Idee von Getter-Setter-Methoden: protected und private Attribute zu
    #Konsequenz: Für jedes Attribut 1 Setter und ein Getter
    #Getter / Setter werden nicht in UML modelliert


    def getName(self):  #Lese-Metrhode, diese Mthode ist public
        return self.__name

    def setName(self,wert): #Schreiben
        #Hier kann man eine Zugriffslogik implementieren (Kontrolle ausüben)

        if wert == "Hallo":
            print("Fehlermeldung")
        else:
            self.__name = wert # Zuweisung







m = Mitarbeiter("Schmidt","-5000")

print(m.getName())
m.setName("Hallo")
print(m.getName())




#print(m.name)
print(m._abteilung) # !!!!!!!!!!!!!!!

#print(m.__gehalt)
print(m._Mitarbeiter__gehalt) # ???!!!!!!!!!!!!!!!!!
