# Recebe um numero n e uma lista e retorna uma sublista de numeros que
# são maiores que n da lista

def maioresQue(n, xs):
    lista = []
    for x in xs:
        if x > n:
            lista.append(x)
    return lista

print(maioresQue(10, []) == []) #True
print(maioresQue(10, [11,9,12]) == [11,12]) #True
print(maioresQue(10, [4,6,30,3,15,3,10,7]) == [30,15]) #True