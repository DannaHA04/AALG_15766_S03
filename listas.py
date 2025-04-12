a = ["Juan", 20, 1.8, True]

print(a[len(a)-1])
print(a[-1]) #Esto imprime el ultimo valor de la lista
print(a[-2]) #Esto imprime el penultimo valor de la lista

b = [4, 2, 6, 3]

print(len(b)) #Cuantos elementos tiene la lista
print(sum(b)) #La suma de los elementos de la lista
print(max(b)) #el maximo de la lista
print(min(b)) #el minimo de la lista
print(sum(b) / len(b)) # el promedio

c = a + b

print(c) #Sale concatenado

# Para imprimir los elementos de la lista
for x in b:
    print(x) 

#DESTRUCTURACION
p= "mesa"
q = "silla"
print(p,q)
tmp = p
p = q
q = tmp
print(p,q)
p,q = q,p
print(p,q)


def suma5(e,f):
    return e + 5, f + 5
print(suma5(2,5))

x,y = suma5(2,5)
print(x,y)

busca = 6

if busca in b: #[4,2,6,3]
    print("Encontrado")

