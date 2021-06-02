# Soma todos os números ímpares de uma lista

def somaImpares(xs):
    cont = 0
    for x in xs:
        if x % 2 != 0:
            cont += x
    return cont

print(somaImpares ([2,3,1,5]) == 9) #True
print(somaImpares ([1,1,4,2]) == 2) #True
print(somaImpares ([3,2,4,6,5,7,8,0,1]) == 16) #True
print(somaImpares ([2,3,1,5,2,2]) == 9) #True
print(somaImpares ([1,1,1,1]) == 4) #True