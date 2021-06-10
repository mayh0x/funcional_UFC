# Recebe uma lista e retorna uma versão acumulativa da lista
# Na versão acumulativa, soma-se as todas as chaves de u até a posição k

def listacc(xs):
    if xs == []:
        return []
    if len(xs) == 1:
        return xs
    tira_final = xs[:-1]
    return listacc(tira_final) + [sum(xs)]

print(listacc([]) == []) #True
print(listacc([1]) == [1]) #True
print(listacc([1,3,4]) == [1,4,8]) #True
print(listacc([4,3,1,1]) == [4,7,8,9]) #True
print(listacc([1,2,3,4]) == [1,3,6,10]) #True