#Westermann S. 198, Aggregation

class Auto:


    def __init__(self): # Konstruktor

        self.marke = "Mercedes"
        self.alle_raeder = [] # Leere Liste

    def reifenmontieren(self, reifen):
        self.alle_raeder.append(reifen) # Reifen hinzugefügt
        print("Ein Reifen ist montiert")




class ContinentalReifen():

    reifennummer = ""

    def __init__(self):
        self.reifennummer = "ContinalReifen"

# Ein Auto ohne Reifen
mein_mercedes = Auto()
mein_mercedes2 = Auto()

print(mein_mercedes.alle_raeder) # leere Liste

#Reifen herstellen und an das Auto
#technisch: Kaskadierung von Methodenaufrufen

reifen1 = ContinentalReifen()

mein_mercedes.reifenmontieren(reifen1)
mein_mercedes.reifenmontieren(ContinentalReifen())


print(mein_mercedes.alle_raeder[0].reifennummer) # Zugriff in Liste mit Index
print(mein_mercedes.alle_raeder[1].reifennummer)

print(mein_mercedes)

if mein_mercedes == mein_mercedes2:
    pass
