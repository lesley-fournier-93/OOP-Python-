class WetterAppCelsius:
    """Die Erwartung unserer App: Daten in JSON und Grad Celsius."""

    def zeige_daten(self):
        pass


class USWetterDienst:
    """Der fremde Dienst liefert XML und nutzt Grad Fahrenheit."""

    def hole_xml_daten(self):
        # 68°F entsprechen 20°C
        return "<wetter><temp>68</temp><stadt>New York</stadt></wetter>"


class WetterAdapter(WetterAppCelsius):
    """Der Adapter übersetzt Format UND Maßeinheit."""

    def __init__(self, us_dienst):
        self.us_dienst = us_dienst

    def zeige_daten(self):
        # 1. Daten vom fremden Dienst holen
        xml = self.us_dienst.hole_xml_daten()

        # 2. Extraktion (vereinfacht) und Umrechnung
        # Formel: (F - 32) * 5/9 = C
        temp_f = 68
        temp_c = (temp_f - 32) * 5 / 9

        stadt = "New York"

        # 3. Rückgabe im von der App erwarteten Format
        return f'{{"temperatur_celsius": {temp_c:.1f}, "stadt": "{stadt}"}}'


# --- Test der Erweiterung ---
us_service = USWetterDienst()
adapter = WetterAdapter(us_service)

print("App empfängt konvertierte Daten:")
print(adapter.zeige_daten())
