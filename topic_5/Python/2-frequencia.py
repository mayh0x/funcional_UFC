# Recebe uma lista e um valor n e retorna o total de ocorrências de x

def frequencia(n, xs):
    cont = 0
    for x in xs:
        if x == n:
            cont += 1
    return cont

print(frequencia(1, []) == 0) #True
print(frequencia(4, [4]) == 1) #True
print(frequencia(4, [5]) == 0) #True
print(frequencia(4, [4,4]) == 2) #True
print(frequencia(2, [4,4]) == 0) #True
print(frequencia(5, [4,5,2,1,5,5,9]) == 3) #True