from functools import singledispatchmethod

class Rechner:
  @singledispatchmethod # Dekorator für die Methode
  def add(self, x):
    print("Standard:", x)

  @add.register
  def _(self, x:int):
    print("Int", x + 10)

  @add.register
  def _(self, x: str):
    print("String", x + "!!!")

r = Rechner()
r.add(5) 
r.add("Hallo")
r.add(3.14)

 #singledispatchmethod = nur einen Parameter matchen, aber verschiedene Typen, d.h. Überladung von Methoden, aber nur mit einem Parameter, da es sonst zu Mehrdeutigkeiten kommen könnte, wenn mehrere Parameter den selben Typ haben, aber unterschiedliche Bedeutungen, z.B. add(5, 10) könnte sowohl als add(int, int) als auch als add(float, float) interpretiert werden, was zu einem Fehler führen würde. 