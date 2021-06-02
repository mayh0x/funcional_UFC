# Recebe duas listas e retorna a intercessão entre elas

def intersec(xs, ys):
    lista = []
    for x in xs:
        for y in ys:
            if x == y:
                lista.append(x)
    return lista

# def intersec(xs, ys):
#    lista = []
#    lista = xs.intersection(ys)

print(intersec ([3], [3]) == [3]) #True
print(intersec ([3,4,1], [1,4,3]) == [3,4,1]) #True
print(intersec ([3,6,5,7], [9,7,5,1,3,6]) == [3,6,5,7]) #True
print(intersec ([3,6,5,7], [9,7,5,1,3]) == [3,5,7]) #True