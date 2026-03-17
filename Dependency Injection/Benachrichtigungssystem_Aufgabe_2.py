'''
Aufgabe 2: Benachrichtigungssystem mit wechselnden Versandkanälen
Ein Unternehmen möchte ein Benachrichtigungssystem entwickeln. Eine Klasse 
'NotificationService' soll Nachrichten versenden können. Der Versand kann per E-Mail, SMS 
oder (für besonders nostalgische Kunden) per Fax erfolgen.
a) Entwerfen Sie zunächst eine naive Implementierung, bei der der Versandkanal direkt 
innerhalb der Klasse instanziiert wird.
b) Refaktorieren Sie die Implementierung unter Verwendung von Dependency Injection, 
sodass der Versandkanal von außen übergeben wird.
c) Schreiben Sie einen einfachen Unit-Test, der mithilfe eines Mock-Objekts überprüft, ob 
der Versand korrekt ausgelöst wird, ohne tatsächlich eine SMS oder ein Fax zu verschicken.
Ziel ist es, die Testbarkeit und Erweiterbarkeit des Systems durch DI zu verbessern.

'''

#a) Naive Implementierung (ohne DI) - NotificationService entscheidet selbst, welchen Kanal er nutzt, und instanziiert ihn intern.

class EmailSender:
    def send(self, message: str, recipient: str) -> None:
        print(f"[EMAIL] To: {recipient} | {message}")


class SMSSender:
    def send(self, message: str, recipient: str) -> None:
        print(f"[SMS] To: {recipient} | {message}")


class FaxSender:
    def send(self, message: str, recipient: str) -> None:
        print(f"[FAX] To: {recipient} | {message}")


class NotificationService:
    def __init__(self, channel: str):
        # Harte Kopplung: Service entscheidet & baut den Sender selbst
        if channel == "email":
            self.sender = EmailSender()
        elif channel == "sms":
            self.sender = SMSSender()
        elif channel == "fax":
            self.sender = FaxSender()
        else:
            raise ValueError("Unknown channel")

    def notify(self, message: str, recipient: str) -> None:
        self.sender.send(message, recipient)


service = NotificationService("sms")
service.notify("Dein Code ist deployt.", "+49 170 1234567")

'''
Probleme:
- Neue Kanäle → NotificationService muss geändert werden (schlecht erweiterbar)

- Unit-Tests schwierig (weil echte Sender erzeugt werden)

- Viele if/elif-Zweige wachsen mit jedem Kanal

'''

# b) Refaktorierung mit Dependency Injection (Konstruktor-Injektion)- bekommt Service von außen übergeben

from typing import Protocol


class Sender(Protocol):
    def send(self, message: str, recipient: str) -> None:
        ...


class EmailSender:
    def send(self, message: str, recipient: str) -> None:
        print(f"[EMAIL] To: {recipient} | {message}")


class SMSSender:
    def send(self, message: str, recipient: str) -> None:
        print(f"[SMS] To: {recipient} | {message}")


class FaxSender:
    def send(self, message: str, recipient: str) -> None:
        print(f"[FAX] To: {recipient} | {message}")


class NotificationService:
    def __init__(self, sender: Sender):
        self.sender = sender

    def notify(self, message: str, recipient: str) -> None:
        self.sender.send(message, recipient)


# Verwendung: Kanal austauschbar ohne NotificationService anzufassen
service_sms = NotificationService(SMSSender())
service_sms.notify("Deine TAN ist 123456.", "+49 170 1234567")

service_fax = NotificationService(FaxSender())
service_fax.notify("Bitte unterschreiben und zurückfaxen.", "+49 30 123456")


# c) Unit-Test mit Mock (ohne echte SMS/Fax) - einfacher Unit Test - unittest + unittest.mock.Mock

import unittest
from unittest.mock import Mock


class NotificationService:
    def __init__(self, sender):
        self.sender = sender

    def notify(self, message: str, recipient: str) -> None:
        self.sender.send(message, recipient)


class TestNotificationService(unittest.TestCase):
    def test_notify_triggers_send_once_with_correct_args(self):
        # Arrange: Mock-Sender statt echter SMS/Fax
        mock_sender = Mock()
        service = NotificationService(mock_sender)

        # Act
        service.notify("Hallo!", "012345")

        # Assert: Wurde send korrekt ausgelöst?
        mock_sender.send.assert_called_once_with("Hallo!", "012345")


if __name__ == "__main__":
    unittest.main()

'''
Was der Test beweist:

- NotificationService.notify() ruft send() genau einmal auf

- mit den richtigen Argumenten

- ohne tatsächlich SMS, Fax oder E-Mail zu verschicken

'''




