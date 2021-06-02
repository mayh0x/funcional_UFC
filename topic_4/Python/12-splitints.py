# Recebe uma lista e retorna uma tupla com uma lista de ímpares
# e outra lista de pares

def splitints(xs):
    listaimpar = []
    listapar = []
    tupla = ()
    for x in xs:
        if x % 2 != 0:
            listaimpar.append(x)
        if x % 2 == 0:
            listapar.append(x)
    tupla = (listaimpar, listapar)
    return tupla

print(splitints ([1,2,3,4,5,6,7]) == ([1,3,5,7],[2,4,6])) #True
print(splitints ([2,4,6,1,1,7]) == ([1,1,7],[2,4,6])) #True