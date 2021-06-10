# Remove a primeira ocorrência de um número numa lista

def deletee(n, xs):
    cont = 0
    lista = []
    for x in xs:
        if x == n:
            cont += 1
        if cont < 1 or cont > 1 or x != n:
            lista.append(x)
    return lista

print(deletee(5, []) == []) #True
print(deletee(1, [1]) == []) #True
print(deletee(4, [1,3,4]) == [1,3]) #True
print(deletee(3, [4,3,1,3]) == [4,1,3]) #True
print(deletee(5, [1,5,6,9]) == [1,6,9]) #True