#LISTAS COMPRENSIVAS

#Esto es una lista intensional en Python
a = [2 * x for x in range (1, 10+1)]
print(a)

print([n for n in range(1,10,2)])

#Lista comprensivas
x = [0 if n % 3 == 0 else n for n in range(1, 10, 2)]
print(x)

