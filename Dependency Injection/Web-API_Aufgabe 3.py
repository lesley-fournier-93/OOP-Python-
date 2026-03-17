'''
Aufgabe 3: Web-API mit austauschbarer Datenquelle
Sie entwickeln eine kleine Web-API, die Produktdaten bereitstellt. Die Klasse 
'ProductController' greift auf eine Datenquelle zu, um Produkte zu laden.
a) Implementieren Sie eine Version, in der der Controller direkt eine konkrete Klasse 
'DatabaseRepository' verwendet.
b) Refaktorieren Sie die Implementierung so, dass ein abstraktes Repository-Interface 
verwendet wird und die konkrete Implementierung per Dependency Injection erfolgt.
c) Implementieren Sie zusätzlich eine alternative Datenquelle 'InMemoryRepository' für 
Testzwecke und demonstrieren Sie deren Verwendung.
Erläutern Sie abschließend in wenigen Sätzen, welche Vorteile Dependency Injection in 
Bezug auf Wartbarkeit, Austauschbarkeit und Testbarkeit bietet

'''

# a) Naive Version: Controller nutzt direkt DatabaseRepository - Hier hängt der Controller direkt an einer konkreten Implementierung → harte Kopplung.

class DatabaseRepository:
    def get_all_products(self) -> list[dict]:
        # Stell dir vor: SQL-Abfrage, ORM, etc.
        return [
            {"id": 1, "name": "Coffee Beans", "price": 7.99},
            {"id": 2, "name": "Milk Frother", "price": 19.90},
        ]


class ProductController:
    def __init__(self):
        # Harte Abhängigkeit: Controller instanziiert selbst die DB-Quelle
        self.repo = DatabaseRepository()

    def list_products(self) -> dict:
        products = self.repo.get_all_products()
        # typische API-Response-Struktur
        return {"count": len(products), "items": products}


controller = ProductController()
print(controller.list_products())

# Problem: Wenn du statt DB eine Datei / API / InMemory fürs Testing willst, musst du den Controller ändern.

# b) Refaktorierung: Repository-Interface + Dependency Injection

from typing import Protocol


class ProductRepository(Protocol):
    def get_all_products(self) -> list[dict]:
        ...


class DatabaseRepository:
    def get_all_products(self) -> list[dict]:
        return [
            {"id": 1, "name": "Coffee Beans", "price": 7.99},
            {"id": 2, "name": "Milk Frother", "price": 19.90},
        ]


class ProductController:
    def __init__(self, repo: ProductRepository):
        # DI: Controller bekommt Repository von außen
        self.repo = repo

    def list_products(self) -> dict:
        products = self.repo.get_all_products()
        return {"count": len(products), "items": products}



controller = ProductController(DatabaseRepository())
print(controller.list_products())

# c) Alternative Datenquelle: InMemoryRepository + Verwendung

class InMemoryRepository:
    def __init__(self, initial_data: list[dict] | None = None):
        self._products = initial_data or []

    def get_all_products(self) -> list[dict]:
        return list(self._products)  # Kopie zurückgeben


# Demo: Controller mit InMemory (ohne Codeänderung am Controller)
test_data = [
    {"id": 101, "name": "Test Product A", "price": 1.23},
    {"id": 102, "name": "Test Product B", "price": 4.56},
]

controller_test = ProductController(InMemoryRepository(test_data))
print(controller_test.list_products())

'''
Vorteile von Dependency Injection (kurz erklärt)

- Wartbarkeit: Der Controller bleibt simpel und enthält keine DB-/Technologie-Logik. Änderungen an der Datenquelle betreffen nur die  Repository-Klassen.

- Austauschbarkeit: Neue Datenquellen (z. B. ApiRepository, FileRepository) können hinzugefügt werden, ohne den Controller anzufassen.

- Testbarkeit: Für Unit-Tests kann man ein InMemoryRepository oder ein Mock-Repository injizieren – keine echte Datenbank, keine komplizierten Setups, schnelle Tests.
'''
