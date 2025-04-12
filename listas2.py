w = []
print(w)
w.append("d")
w.insert(0,"b") # Asignarle valor a una posicion dada
w.append("f")
print(w)

print(w.index("d")) #Para saber en que posicion está
del w[1] #para eliminar un valor de la lista

w.remove("b")
print(w)


#TUPLES
#importante no se puede modificar
t = ("r", "s", "t")
print(t)

#Convertir tuple a lista
v = list(t)

#Convertir la lista a tuple
s = tuple(v)


