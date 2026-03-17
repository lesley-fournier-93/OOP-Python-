# 1. Kreis-Funktion gezielt importieren
from geometrie import kreis_flaeche

# 2. Gesamtes Modul unter Alias importieren
import geometrie as geo


def main():
    print("Geometrie-Rechner")

    # Kreis
    radius = float(input("Radius des Kreises: "))
    kreis_ergebnis = kreis_flaeche(radius)
    print(f"Fläche des Kreises: {kreis_ergebnis:.2f}")

    print()

    # Rechteck
    laenge = float(input("Länge des Rechtecks: "))
    breite = float(input("Breite des Rechtecks: "))
    rechteck_ergebnis = geo.rechteck_flaeche(laenge, breite)
    print(f"Fläche des Rechtecks: {rechteck_ergebnis:.2f}")


if __name__ == "__main__":
    main()