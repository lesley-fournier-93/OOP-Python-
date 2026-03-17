'''
Aufgabe 4: Polymorphie in einem spielerischen Kontext (Tiergeräusche im Zoo)

Sie entwickeln eine kleine Anwendung für einen digitalen Zoo. Unterschiedliche Tiere sollen Geräusche von sich geben.

a) Implementieren Sie eine Basisklasse „Tier“ mit einer Methode „mache_geraeusch()“.

b) Leiten Sie mehrere Tierklassen (z.B. Hund, Katze, Papagei) ab und überschreiben Sie die Methode entsprechend.

c) Erstellen Sie eine Funktion „zoo_show(tiere)“, die für alle übergebenen Tiere das jeweilige Geräusch ausgibt.

d) Erweitern Sie das System um ein weiteres Tier, ohne die bestehende Show-Funktion zu verändern.

'''

class Tier:
    def mache_geraeusch(self):
        pass


class Hund(Tier):
    def mache_geraeusch(self):
        return "Wuff!"


class Katze(Tier):
    def mache_geraeusch(self):
        return "Miau!"


class Papagei(Tier):
    def mache_geraeusch(self):
        return "Krah!"


def zoo_show(tiere):
    for tier in tiere:
        print(tier.mache_geraeusch())


# Jetzt erweitern wir direkt die Liste
class Elefant(Tier):
    def mache_geraeusch(self):
        return "Töröö!"


tiere = [Hund(), Katze(), Papagei(), Elefant()]

zoo_show(tiere)

