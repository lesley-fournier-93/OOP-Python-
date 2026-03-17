from abc import ABC, abstractmethod

# Subject (FootballMatch)
class FootballMatch:
    def __init__(self, home_team, away_team):  # Konstruktor
        self._observers = []  # Registrierliste
        self._home_team = home_team
        self._away_team = away_team
        self._home_goals = 0
        self._away_goals = 0

    def add_observer(self, observer):  # Anmeldung
        self._observers.append(observer)

    def remove_observer(self, observer):  # Abmeldung
        self._observers.remove(observer)

    def notify_observers(self):  # alle Observer benachrichtigen
        score = f"{self._home_team} {self._home_goals}:{self._away_goals} {self._away_team}"
        for observer in self._observers:
            observer.update(score)

    # Tor Heimteam
    def goal_home(self):
        self._home_goals += 1
        self.notify_observers()

    # Tor Auswärtsteam
    def goal_away(self):
        self._away_goals += 1
        self.notify_observers()


# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, score: str):
        pass


# Concrete Observer: Mobile App
class MobileApp(Observer):
    def update(self, score):
        teile = score.split()
        team1 = teile[0]
        ergebnis = teile[1]
        team2 = teile[2]

        home_goals = ergebnis.split(":")[0]
        away_goals = ergebnis.split(":")[1]

        print(f"Mobile App: Neuer Spielstand = {team1} {home_goals}: {away_goals} {team2}")


# Concrete Observer: Web Portal
class WebPortal(Observer):
    def update(self, score):
        teile = score.split()
        team1 = teile[0]
        ergebnis = teile[1]
        team2 = teile[2]

        home_goals = int(ergebnis.split(":")[0])
        away_goals = int(ergebnis.split(":")[1])

        if home_goals > away_goals:
            print(f"Web Portal: {team1} führt mit {home_goals}:{away_goals} gegen {team2}")
        elif away_goals > home_goals:
            print(f"Web Portal: {team2} führt mit {away_goals}:{home_goals} gegen {team1}")
        else:
            print(f"Web Portal: Ausgleich! {team1} {home_goals}:{away_goals} {team2}")

#Concrete Observer: TV Channel

class TVChannel(Observer):
    def update(self, score):
        print(f"TV Channel: Live-Kommentar zum neuen Spielstand: {score}")

# Client code
if __name__ == "__main__":

    # Subject
    football_match = FootballMatch("Bayern", "Dortmund")

    # Observer
    mobile_app = MobileApp()
    web_portal = WebPortal()
    tv_channel = TVChannel()

    # Observer registrieren
    football_match.add_observer(mobile_app)
    football_match.add_observer(web_portal)
    football_match.add_observer(tv_channel)

    # Tor-Events
    football_match.goal_home()   # Bayern 1:0 Dortmund
    football_match.goal_away()   # Bayern 1:1 Dortmund