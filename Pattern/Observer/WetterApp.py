class WetterAppCelsius:
    """Die Ziel-Schnittstelle"""

    def zeige_daten(self):
        return "Standard JSON Daten"


class USWetterDienst:
    """Die zu adaptierende Klasse (Adapter)"""

    def hole_xml_daten(self):
        return "<wetter><temp>68</temp><stadt>New York</stadt></wetter>"


# Der Adapter nutzt Mehrfachvererbung:
# - WetterAppCelsius = Ziel-Schnittstelle
# - USWetterDienst = adaptierte Klasse
class WetterKlassenAdapter(WetterAppCelsius, USWetterDienst):

    def zeige_daten(self):
        # 1. XML-Daten vom US-Dienst holen
        xml = self.hole_xml_daten()

        # 2. Werte aus dem XML lesen (hier vereinfacht)
        temp_f = 68
        stadt = "New York"

        # 3. Fahrenheit in Celsius umrechnen
        temp_c = (temp_f - 32) * 5 / 9

        # 4. JSON-String im gewünschten Format zurückgeben
        return f'{{"temperatur_celsius": {temp_c:.1f}, "stadt": "{stadt}"}}'



adapter = WetterKlassenAdapter()
print(adapter.zeige_daten())