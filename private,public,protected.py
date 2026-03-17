#private,public, protected

class Mitarbeiter:

    def __init__(self, p_name, gehalt):
        self.name = p_name
        self._abteilung = "IT"
        self.__gehalt = gehalt 

    def zeige_info(self):
        print(f"{self.name}, {self._abteilung}")

    def __berechne_bonus(self):
        return self.__gehalt * 0.1

    def get_gehalt(self):
        return self.__gehalt


m = Mitarbeiter("Schmidt", 50000)

print(m.name)
print(m._abteilung)
print(m.get_gehalt())