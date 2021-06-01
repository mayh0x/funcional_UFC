# Recebe uma lista e um número n e retorna uma tupla de listas
# onde a tupla 1 é formada pelos primeiros n elementos da lista
# e a tupla 2 formada pelo restante

def divide(xs, n):
    lista1 = []
    lista2 = []
    tupla = ()
    index = 0
    for x in xs:
        if index < n:
            lista1.append(x)
            index += 1
        else:
            lista2.append(x)
    tupla = (lista1, lista2)
    return tupla
    

print(divide ([1,2,3,4], 0) == ([],[1,2,3,4])) #True
print(divide ([1,2,3,4], 1) == ([1],[2,3,4])) #True
print(divide ([1,2,3,4], 2) == ([1,2],[3,4])) #True
print(divide ([1,2,3,4], 3) == ([1,2,3],[4])) #True
print(divide ([1,2,3,4], 4) == ([1,2,3,4],[])) #True