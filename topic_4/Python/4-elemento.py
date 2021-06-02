# Recebe uma lista e um numero n e retorna o n-ésimo termo da lista

def elemento(n, xs):
    for x in xs:
        if(x == xs[n]):
            return x

print(elemento (2, [2,7,3,9]) == 3) #True
print(elemento (0, [2,7,3,9]) == 2) #True
print(elemento (-1, [2,7,3,9]) == 9) #True
print(elemento (-2, [2,7,3,9]) == 3) #True