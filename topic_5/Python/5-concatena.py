# Recebe duas listas e retorna a concatenação delas

def concatena(xs, ys):
    lista = []
    for x in xs:
        lista.append(x)
    for y in ys:
        lista.append(y)
    return lista

print(concatena([], []) == []) #True
print(concatena([], [3,4]) == [3,4]) #True
print(concatena([1,2], []) == [1,2]) #True
print(concatena([1,2], [3,4]) == [1,2,3,4]) #True
print(concatena([1,2,3], [3,4]) == [1,2,3,3,4]) #True