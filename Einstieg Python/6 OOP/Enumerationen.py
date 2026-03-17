import enum
class Farbe(enum.IntEnum):
 rot = 5
 gelb = 2
 blau = 4
x = 2
if x == Farbe.gelb:
 print("Das ist gelb")
print(Farbe.gelb)
print(Farbe.gelb * 10)