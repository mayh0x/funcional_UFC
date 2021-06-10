# Recebe um inteiro e os números até ele (com os negativos desses numeros)

def alter(n):
    lista = []
    aux = -1
    cont = 1
    while(cont <= n):
        lista.append(cont)
        lista.append(aux)
        cont += 1
        aux -= 1
    return lista

print(alter(1) == [1,-1]) #True
print(alter(2) == [1,-1,2,-2]) #True
print(alter(4) == [1,-1,2,-2,3,-3,4,-4]) #True