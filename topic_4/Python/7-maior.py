# Recebe uma lista e retorna o maior valor da lista

def maior(xs):
    valor = 0
    for x in xs:
        if int(x) > valor:
            valor = int(x)
    return valor

print(maior ([4]) == 4) #True
print(maior ([5,1]) == 5) #True
print(maior ([5,7]) == 7) #True
print(maior ([1,2,7,1,5]) == 7) #True
print(maior ([1,2,3,1,5]) == 5) #True