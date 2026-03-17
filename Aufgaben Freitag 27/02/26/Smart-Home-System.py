'''
Aufgabe 1: Das modulare Smart-Home-System
Kontext:
Ein Unternehmen für Gebäudeautomatisierung benötigt eine Software zur Steuerung verschiedener
Endgeräte (Licht, Heizung, Sicherheitssensoren). Das System muss hochgradig erweiterbar sein, um
zukünftig neue Gerätetypen ohne Änderung des Kerncodes zu unterstützen.

Ihre Aufgaben:

Modellierung (UML):
Entwerfen Sie ein Klassendiagramm. Nutzen Sie eine abstrakte Basisklasse SmartDevice und
leiten Sie konkrete Klassen wie Light und Thermostat ab. Integrieren Sie eine Steuerzentrale
(Hub), die eine Liste von Geräten verwaltet.

Algorithmus (PAP/Pseudocode):
Erstellen Sie einen Ablaufplan für eine Methode anwesenheitssimulation(). Diese soll alle
registrierten Geräte durchlaufen und je nach Gerätetyp unterschiedliche Aktionen ausführen
(Polymorphie).

Implementierung in Python:

Vererbung & Sichtbarkeit: Nutzen Sie geschützte Attribute (z. B. _status) und private
Attribute für kritische Daten (z. B. __seriennummer).

Getter/Setter: Implementieren Sie Properties für die Temperatursteuerung inklusive
Validierung (z. B. keine Werte über 30°C).

Überschreiben: Jedes Gerät soll eine Methode reagiere_auf_notfall() unterschiedlich
implementieren.

SOLID: Achten Sie insbesondere auf das Dependency Inversion Principle: Die Zentrale soll nur
gegen das Interface SmartDevice arbeiten, nicht gegen konkrete Lampen oder Heizungen.

Zeitansatz: ca. 120 Minuten

'''

from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name, seriennummer):
        self.name = name
        self._status = False
        self.__seriennummer = seriennummer

    def einschalten(self):
        self._status = True

    def ausschalten(self):
        self._status = False

    @abstractmethod
    def reagiere_auf_notfall(self):
        pass

    @abstractmethod
    def aktion(self):
        pass
   

class Light(SmartDevice):
  
    def __init__(self, name, seriennummer):
        super().__init__(name, seriennummer)

    def reagiere_auf_notfall(self):
        return "Das Licht blinkt rot."

    def aktion(self):
        return "Das Licht geht kurz an und wieder aus."


class Thermostat(SmartDevice):
    def __init__(self, name, seriennummer, start_temp):
        super().__init__(name, seriennummer)
        self.__temperature = start_temp

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value > 30:
          raise ValueError("Die Temperatur darf nicht über 30°C liegen.")
        self.__temperature = value

    def reagiere_auf_notfall(self):
        return "Die Heizung schaltet sich aus."

    def aktion(self):
        self.temperature = min(self.temperature + 1, 30)
        return f"Die Temperatur wird auf {self.temperature}°C erhöht."
  
class SecuritySensor(SmartDevice):
    def __init__(self, name, seriennummer):
        super().__init__(name, seriennummer)
        self.triggered = False

    def aktion(self):
        return "SecuritySensor prüft Status (Simulation)."

    def reagiere_auf_notfall(self):
        self.triggered = True
        return "SecuritySensor: Alarm ausgelöst!"


class Hub:
    def __init__(self):
        self._devices = []

    def add_device(self, device):
        self._devices.append(device)
    
    def remove_device(self, device):
      if device in self._devices:
        self._devices.remove(device)

    def anwesenheitssimulation(self):
        for device in self._devices:
            print(device.aktion())

    def notfall_melden(self):
        for device in self._devices:
            print(device.reagiere_auf_notfall())


# Test
hub = Hub()
hub.add_device(Light("Wohnzimmerlicht", "SN-1234"))
hub.add_device(Thermostat("Heizung", "SN-9999", 22))
hub.add_device(SecuritySensor("Türsensor", "SN-0001"))

hub.anwesenheitssimulation()
hub.notfall_melden()
  