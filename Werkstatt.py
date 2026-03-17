
# Grundsätzlich: 
'''
1.) Problem verstehen
2.) Probleme in Teilprobleme/Teilaufgaben zerlegen
3.) Teillösungen finden (PAP/Pseudocode,...)
4.) Technische Bauteile für die Einzelprobleme suchen: z.B. While-Schleife, For-Schleife,...
5.) Dann einzelne Lösungen programmieren 
6.) Gesamtlösung programmieren 

'''

class Klassenname:
  
  # 1. Konstruktor/Attribute
  # 2. Methoden: beschleunigen, bremsen, einsteigen
  # 3. Getter/Setter Methoden

  def hdjdhjdhdd(self):
    print("Hallo")
  def jxghjgdshdfsgd(self):
    pass


i = 9
print(type(i))

class Fahrzeug:
  # geschwindigkeit = 0  Klassenvariable/Klassenattribut = für alle Objekte gleich = Objekte teilen sich ein Atrribut

  # Konstruktor?? => Eigentliche Aufgabe: Initialisierung von Attributen
  # ohne expliziten Konstruktor, wird der Standardkonstruktor verwendet,
  # der aber nur deklariert (nur Speicherplatz vergibt)

  def __init__(self, ge = 0): # expliziter Konstruktor mit einem Default-Parameter / Grundsätzlich mit Konstruktor programmieren, damit
    self.geschwindigkeit = ge

  def beschleunigen(self, wert): # überschattet
    self.geschwindigkeit += wert # hier Geschwindigkeit = Objektattribut, da es mit self. definiert ist, d.h. jedes Objekt hat sein eigenes Geschwindigkeit-Attribut                                  
  
  def ausgabe(self):
    pass

f1 = Fahrzeug() #f1: Objekt, Fahrzeug() Konstruktoraufruf
print(f1.geschwindigkeit)

f1.beschleunigen(55)

f1.beschleunigen(45,33) # wird ausgeführt und überschattet die vorherige Methode, da sie den selben Namen hat, aber andere Parameter

print(type(f1))