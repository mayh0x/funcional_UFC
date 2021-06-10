# Recebe duas listas e retorna uma lista com os elementos intercalados

def uniao(xs, ys):
    lista = []
    for x in xs:
        lista.append(x)
    for y in ys:
        if y not in lista:
            lista.append(y)
    return lista

def intercal(xs, ys):
    lista = [*sum(zip(xs,ys),())]
    tam = len(xs) + len(ys)
    if len(lista) < tam:
        if len(xs) > len(ys):
            lista = uniao(lista, xs)
        elif len(xs) < len(ys):
            lista = uniao(lista, ys)
    return lista
    
print(intercal([1,2,3], [7,8,9]) == [1,7,2,8,3,9]) #True
print(intercal([1,2,3,4], [8,9]) == [1,8,2,9,3,4]) #True
print(intercal([5], [1,2,6]) == [5,1,2,6]) #True