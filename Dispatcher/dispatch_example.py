# Python program to demonstrate
# dispatch decorator

from multipledispatch import dispatch



'''def addiere(a: int,b: int): # Annotation
    summe = a + b
    return summe


print(addiere(4,5)) # Addition
print(addiere("Hall","o")) #Konkatenieren
print(addiere(4.0,6.5))'''




@dispatch(int,str) #Dekorator
def func(x,c):
    print("Integer1" + c)
    return x * 2

@dispatch(float)
def func(x):
    print("Float")
    return x / 2

@dispatch(str) # Dekorator
def func(x):
    print("String")
    return ("Einen String")


'''def addieren(x, y):
    erg = x + y

def addieren(x):
    y = 7
    erg = x + y'''



# Driver code
print(func(2.0))


print(func(2,"joj"))


print(func("Hallo"))