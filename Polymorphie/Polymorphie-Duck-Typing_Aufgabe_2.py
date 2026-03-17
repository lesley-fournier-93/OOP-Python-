'''
Aufgabe 2: Polymorphie durch Duck Typing (Benachrichtigungssystem)

Sie entwickeln ein Benachrichtigungssystem, das Nachrichten über verschiedene Kanäle versendet (z.B. E-Mail, SMS, Push-Nachricht).

a) Implementieren Sie drei Klassen mit jeweils einer Methode „senden(nachricht)“.

b) Entwickeln Sie eine Funktion, die ein beliebiges Objekt akzeptiert und die Methode „senden()“ aufruft, ohne eine gemeinsame Basisklasse zu verwenden.

c) Erläutern Sie, weshalb es sich hierbei um Polymorphie handelt.

d) Ergänzen Sie einen weiteren Kanal, ohne die bestehende Versandfunktion zu verändern.

'''

class Email:
    def senden(self, nachricht):
        print(f"E-Mail gesendet: {nachricht}")    

class SMS:
    def senden(self, nachricht):
        print(f"SMS gesendet: {nachricht}")

class PushNachricht:
    def senden(self, nachricht):
        print(f"Push-Nachricht gesendet: {nachricht}")  

def benachrichtigung_versenden(benachrichtigung, nachricht):  
    benachrichtigung.senden(nachricht)      

# Beispielverwendung
email = Email() 
sms = SMS()
push = PushNachricht()

benachrichtigung_versenden(email, "Hallo per E-Mail!")
benachrichtigung_versenden(sms, "Hallo per SMS!")
benachrichtigung_versenden(push, "Hallo per Push-Nachricht!")

#d) Erweiterung ohne Änderung der Funktion

class WhatsApp:
    def senden(self, nachricht):
        print(f"WhatsApp gesendet: {nachricht}")

wa = WhatsApp()
benachrichtigung_versenden(wa, "Hallo per WhatsApp!")

'''
c)
Polymorphie bedeutet:

--> Gleicher Methodenname – unterschiedliches Verhalten.

Alle Klassen haben:

- def senden(self, nachricht):

--> Aber jede macht etwas anderes.

--> Und die Funktion weiß NICHT, welchen Typ sie bekommt.

'''

        