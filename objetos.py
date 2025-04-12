import random

class Perro:
    def __init__(self, nombre = "", color = "", edad = 0):
        
        #Atributos
        self._nombre = nombre
        self._color = color
        self._edad = edad

    def Ladrar(self): #Si usas los atributos pones Self caso contrario no lo pongas
        print("Guau")
        
    def Saludo(self):
        return "Pata" if random.randint(0,1) == 0 else "Cola"
    def __str__(self):
        return f"Perro: {self._nombre}, de color {self._color} y {self._edad}"


#Crear un Objeto
'''p = Perro()
p._nombre = "Fido"
print(p._nombre)

q = Perro("Rambo", "Negro", 5)
print(q._nombre)'''


p = Perro("Fido", "Marron", 5)
p.Ladrar()
print(f"Me saludo con la {p.Saludo()}")
print(p)
print()

q = Perro()
p._nombre = "Rambo"
print(q._nombre)
