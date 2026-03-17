

class Fahrzeug:
  def __init__(self, bez, ge): 
    self.bezeichnung = bez
    self.geschwindigkeit = ge
  def __gt__(self, other):
    return self.geschwindigkeit > other.geschwindigkeit
  def __eq__(self, other):
    return self.geschwindigkeit == other.geschwindigkeit
  def __sub__(self, other):
    return self.geschwindigkeit - other.geschwindigkeit
  
opel = Fahrzeug("Opel Admiral", 60)
volvo = Fahrzeug("Volvo Amazon", 45)

if opel > volvo:
    print("Opel ist schneller")

elif opel == volvo:
    print("Beide Autos sind gleich schnell")
  
else:
    print("Volvo ist schneller")
  
differenz = opel - volvo
print(f"Geschwindigkeitsdifferenz: {differenz} km/h")