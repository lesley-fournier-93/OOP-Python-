'''
Aufgabe 3: Dependency Inversion Principle (DIP)

Eine Klasse NotificationService instanziiert direkt ein Objekt der Klasse SmsSender, um Nachrichten zu verschicken. Dadurch ist der Service fest an die SMS-Implementierung gebunden.

Ihre Aufgabe: Entkoppeln Sie die Klassen. Führen Sie ein Interface (oder eine abstrakte Basisklasse) MessageSender ein. Der NotificationService soll nun eine Instanz dieses Interfaces über den Konstruktor erhalten (Dependency Injection).

Ziel: High-Level-Module sollen nicht von Low-Level-Modulen abhängen; beide sollen von Abstraktionen abhängen.

Ausgangslage: Der NotificationService ist hart von der konkreten Klasse SmsSender abhängig. Ein Wechsel auf E-Mail oder Push-Nachrichten ist ohne Code-Änderung im Service nicht möglich.

class SmsSender:

    def send(self, message):
        print(f"Sende SMS: {message}")


class NotificationService:

    def __init__(self):
        # Direkte Abhängigkeit von einer konkreten Implementierung
        self.sender = SmsSender()

    def notify(self, message):
        self.sender.send(message)

'''

from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class SmsSender(MessageSender):
    def send(self, message):
        print(f"Sende SMS: {message}")


class EmailSender(MessageSender):
    def send(self, message):
        print(f"Sende E-Mail: {message}")


class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender  # kommt von außen (Dependency Injection)

    def notify(self, message):
        self.sender.send(message)


# Test mit SMS
sms = SmsSender()
service_sms = NotificationService(sms)
service_sms.notify("Hallo per SMS!")

# Test mit E-Mail
email = EmailSender()
service_email = NotificationService(email)
service_email.notify("Hallo per E-Mail!")