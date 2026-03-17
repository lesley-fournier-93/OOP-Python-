from multipledispatch import dispatch

class Calculator:
    @dispatch(int,int)
    def add(self, a, b):
        print("int + int =", a + b)

    @dispatch(str, str)
    def add(self, a, b):
        print("str + str =", a + b)

    @dispatch(float, float)
    def add(self, a, b):
        print("float + float =", a + b)

c = Calculator()
c.add(1, 2)         # -> int + int = 3
c.add("Hallo", "Welt")   # -> str + str = HiYo
c.add(1.5, 2.5)     # -> float + float = 4.0
