from multipledispatch import dispatch


class Rechner:
    @dispatch(int, int)
    def kombiniere(self, a, b):
        return a + b

    @dispatch(str, str)
    def kombiniere(self, a, b):
        return a + " " + b

    @dispatch(list, list)
    def kombiniere(self, a, b):
        return a + b

    @dispatch(int, float)
    def kombiniere(self, a, b):
        return a * b


r = Rechner()

print("int, int:", r.kombiniere(3, 4))                 # 7
print("str, str:", r.kombiniere("Hallo", "Welt"))      # "Hallo Welt"
print("list, list:", r.kombiniere([1, 2], [3, 4]))     # [1, 2, 3, 4]
print("int, float:", r.kombiniere(3, 2.5))             # 7.5

# Erklären Sie, wie sich Multidispatch vom einfachen singledispatch unterscheidet und 
# welche Einschränkungen dabei zu beachten sind.

'''
Singledispatch entscheidet nur anhand eines Parameters.
Multidispatch entscheidet anhand mehrerer Parameter-Typen.

Einschränkungen:

- Mehrdeutigkeiten bei Vererbungen möglich

- Typen müssen explizit definiert werden

- Nicht Teil der Standardbibliothek

'''
