'''Programmieraufgabe: Implementierung eines Singleton-Konfigurationsmanagers in Python

Ziel der Aufgabe
Ziel der Aufgabe ist es, das Singleton-Entwurfsmuster in Python zu implementieren und anzuwenden. Sie entwickeln eine Klasse, die zentrale Konfigurationseinstellungen eines Programms verwaltet.

Aufgabenstellung
Entwickeln Sie eine Klasse mit dem Namen 'ConfigurationManager'. Diese Klasse soll das Singleton-Pattern verwenden, sodass innerhalb des Programms nur eine einzige Instanz der Klasse existieren kann.

Anforderungen

Implementieren Sie die Klasse 'ConfigurationManager'.

Stellen Sie sicher, dass nur eine Instanz dieser Klasse erzeugt werden kann.

Wenn mehrfach ein Objekt der Klasse erstellt wird, muss stets dieselbe Instanz zurückgegeben werden.

Die Klasse soll eine interne Datenstruktur (z. B. ein Dictionary) zur Speicherung von Konfigurationseinträgen verwenden.

Implementieren Sie eine Methode 'set_config(key, value)', mit der ein Konfigurationswert gesetzt werden kann.

Implementieren Sie eine Methode 'get_config(key)', mit der ein gespeicherter Konfigurationswert abgefragt werden kann.

Falls ein Schlüssel nicht existiert, soll die Methode einen geeigneten Hinweis ausgeben.

Testprogramm

Erstellen Sie anschließend ein kurzes Testprogramm, in dem zwei Variablen jeweils eine Instanz des ConfigurationManager erzeugen. Setzen Sie über eine Instanz einen Konfigurationswert und lesen Sie diesen über die andere Instanz wieder aus. Überprüfen Sie außerdem, ob beide Variablen auf dasselbe Objekt verweisen.

Erwartetes Ergebnis

Das Programm soll zeigen, dass beide Variablen auf dieselbe Instanz der Klasse verweisen. Änderungen an den Konfigurationswerten müssen über beide Referenzen identisch sichtbar sein.'''



class ConfigurationManager(object):

    _instance = None   

    def __init__(self):
        raise RuntimeError("Call instance() instead")


    @classmethod
    def instance(cls):

        if cls._instance is None:
            print("Creating ConfigurationManager")

            cls._instance = cls.__new__(cls)
            cls._instance.config = {}

        return cls._instance


    def set_config(self, key, value):
        self.config[key] = value


    def get_config(self, key):

        if key in self.config:
            return self.config[key]

        return "Key not found"


cm1 = ConfigurationManager.instance()
cm2 = ConfigurationManager.instance()

cm1.set_config("theme", "dark")
cm1.set_config("language", "de")

print(cm2.get_config("theme"))
print(cm2.get_config("language"))

print(cm1)
print(cm2)

print(id(cm1))
print(id(cm2))

print("Are they the same object?", cm1 is cm2)