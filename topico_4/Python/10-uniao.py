# Recebe duas listas e retorna a união entre elas

def uniao(xs, ys):
    lista = []
    for x in xs:
        lista.append(x)
    for y in ys:
        if y not in lista:
            lista.append(y)
    return lista

# def uniao(xs, ys):
#    lista = []
#    lista = xs.union(ys)

print(uniao ([4,5], [1]) == [4,5,1]) #True
print(uniao ([4,5], [4,2,5]) == [4,5,2]) #True
print(uniao ([1,2,3], [2,4,6]) == [1,2,3,4,6]) #True