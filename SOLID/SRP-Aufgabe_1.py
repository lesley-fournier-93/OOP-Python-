'''
Aufgabe 1: Single Responsibility Principle (SRP)

Ihre Aufgabe: Analysieren Sie die Klasse und refaktorisieren Sie den Code. Trennen Sie die Verantwortlichkeiten in drei eigenständige Klassen: UserRepository, EmailService und Logger.

Ziel: Jede Klasse darf nur einen Grund für eine Änderung haben.

Ausgangslage: Die Klasse UserManager ist „zu voll“, da sie Datenhaltung, Kommunikation und Logging vermischt.

class UserManager:

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save_to_db(self):
        print(f"Speichere {self.username} in der Datenbank...")

    def send_welcome_email(self):
        print(f"Sende E-Mail an {self.email}: Willkommen!")

    def log_action(self, action):
        print(f"User {self.username} hat Aktion ausgeführt: {action}\n")

'''

class UserRepository:
    def save_to_db(self, username):
        print(f"Speichere {username} in der Datenbank...")


class EmailService:
    def send_welcome_email(self, email):
        print(f"Sende E-Mail an {email}: Willkommen!")


class Logger:
    def log_action(self, username, action):
        print(f"User {username} hat Aktion ausgeführt: {action}\n")


class UserManager:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.repo = UserRepository()
        self.email_service = EmailService()
        self.logger = Logger()

    def register_user(self):
        self.repo.save_to_db(self.username)
        self.email_service.send_welcome_email(self.email)
        self.logger.log_action(self.username, "Registrierung")



user = UserManager("Schmidt", "schmidt@mail.de")
user.register_user()