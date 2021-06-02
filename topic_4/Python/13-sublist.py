# Retorna uma sublista passando o inicio, o fim e uma lista na qual
# será retirada a sublista

def sublist(i, f, xs):
    lista = []
    tamanho = len(xs)
    if(i < 0):
        i += tamanho

    if(f < 0):
        f += tamanho

    for index, x in enumerate(xs):
        if (index >= i) and (index < f):
            lista.append(x)
        else:
            pass
    return lista

print(sublist (1, 3, [0,1,2,3,4,5,6,7,8,9,10]) == [1,2]) #True
print(sublist (0, 11, [0,1,2,3,4,5,6,7,8,9,10]) == [0,1,2,3,4,5,6,7,8,9,10]) #True
print(sublist (2, 8, [0,1,2,3,4,5,6,7,8,9,10]) == [2,3,4,5,6,7]) #True
print(sublist (0, -1, [0,1,2,3,4,5,6,7,8,9,10]) == [0,1,2,3,4,5,6,7,8,9]) #True
print(sublist (2, -2, [0,1,2,3,4,5,6,7,8,9,10]) == [2,3,4,5,6,7,8]) #True
print(sublist (-10, -1, [0,1,2,3,4,5,6,7,8,9,10]) == [1,2,3,4,5,6,7,8,9]) #True
print(sublist (-4, -2, [0,1,2,3,4,5]) == [2,3]) #True