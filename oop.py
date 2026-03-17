class Auto:
    def __init__(self, marke, farbe, sitze, kilometerstand):
        self.marke = marke
        self.farbe = farbe
        self.sitze = sitze
        self.kilometerstand = kilometerstand

    def kilometerstand_ausgeben(self):
        print(self.kilometerstand)

    def fahren(self, kilometer):
        self.kilometerstand += kilometer
        self.kilometerstand_ausgeben()
   

auto_1 = Auto("BMW", "rot", 5, 30000)
auto_2 = Auto("VW", "blau", 8, 100000)
'''print(auto_1.marke)
print(auto_2.marke)'''

''' auto_1.kilometerstand_ausgeben()
auto_2.kilometerstand_ausgeben() '''

auto_1.fahren(100)
'''print(auto_1.kilometerstand)
print(auto_2.kilometerstand)'''

