import unittest

from logic_fahrzeug import Auto, ElektroAuto, FahrzeugFactory, ElektroFactory


class TestFahrzeugFactory(unittest.TestCase):

    def test_produce_standard_car(self):
        """Die Standard-Factory soll ein Auto erzeugen."""
        fahrzeug = FahrzeugFactory.produce_fahrzeug()

        self.assertIsInstance(
            fahrzeug,
            Auto,
            msg="Die FahrzeugFactory sollte ein Objekt vom Typ 'Auto' erzeugen."
        )

        self.assertEqual(
            fahrzeug.factory_id,
            1234,
            msg="Die factory_id des erzeugten Autos sollte 1234 sein."
        )

    def test_invalid_factory_id(self):
        """Eine falsche Factory-ID soll einen Fehler auslösen."""
        with self.assertRaises(
            RuntimeError,
            msg="Beim Erzeugen eines Autos mit falscher Factory-ID sollte ein RuntimeError entstehen."
        ):
            Auto(f_id=999)

    def test_elektro_factory(self):
        """Die ElektroFactory soll ein ElektroAuto erzeugen."""
        fahrzeug = ElektroFactory.produce_fahrzeug()

        self.assertIsInstance(
            fahrzeug,
            ElektroAuto,
            msg="Die ElektroFactory sollte ein ElektroAuto erzeugen."
        )

        self.assertEqual(
            fahrzeug.factory_id,
            1234,
            msg="Auch Elektroautos müssen die factory_id 1234 besitzen."
        )

    def test_elektro_auto_is_auto(self):
        """Ein ElektroAuto ist auch ein Auto (Vererbung)."""
        fahrzeug = ElektroFactory.produce_fahrzeug()

        self.assertTrue(
            isinstance(fahrzeug, Auto),
            msg="Ein ElektroAuto sollte auch als Auto gelten (Vererbung)."
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
'''Dieser Parameter steuert den Detailgrad der Ausgabe:
Level 0 (Quiet): Man sieht fast nichts, außer dem Endergebnis.
Level 1 (Default): Man sieht einen Punkt . für bestandene Tests, ein F für Fehler (Failures) und ein E für Programmfehler (Errors).
Level 2 (Verbose): Für jeden einzelnen Test wird der Name der Testmethode und deren Ergebnis (z. B. ok) direkt ausgegeben. '''