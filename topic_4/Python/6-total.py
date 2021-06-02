# Recebe uma lista e retorna o total de elementos da lista

def total(xs):
    cont = 0
    for x in xs:
        cont += 1
    return cont

print(total ([]) == 0) #True
print(total ([1]) == 1) #True
print(total ([2,3]) == 2) #True
print(total ([3,2,1]) == 3) #True