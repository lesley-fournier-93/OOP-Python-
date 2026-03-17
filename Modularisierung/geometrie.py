import math

def kreis_flaeche(radius):
    """
    Berechnet die Fläche eines Kreises.
    A = π * r²
    """
    return math.pi * radius ** 2


def rechteck_flaeche(laenge, breite):
    """
    Berechnet die Fläche eines Rechtecks.
    """
    return laenge * breite