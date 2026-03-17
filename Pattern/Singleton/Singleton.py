# What the Gang of Four’s original Singleton Pattern
# might look like in Python.
#https://python-patterns.guide/gang-of-four/singleton/

class Logger(object):
    _instance = None  # protected, Klassenattribut, hier wird das einzige Objekt gespeichert

    def __init__(self):
        raise RuntimeError('Call instance() instead') # der eigentliche Konstruktor wird deaktiviert


    @classmethod
    def instance(cls):  # static
        if cls._instance is None: # gibt es bereits ein Objekt?
            print('Creating new instance')
            cls._instance = cls.__new__(cls) # new erzeugt das Speicherobjekt
            # Put any initialization here.
        return cls._instance


#obj = Logger() - ein Objekt auf normalen Wege erzeugen, den Konstruktor benutzen

#log = Logger() # hier wird versucht ein Objekt zu erzeugen
log1 = Logger.instance()
log2 = Logger.instance()
log3 = Logger.instance()

print(log1)
print(log2)
print(log3)

print(id(log1)) # Speicheradresse überprüfen
print(id(log2))
print(id(log3))


print('Are they the same object?', log1 is log2)




