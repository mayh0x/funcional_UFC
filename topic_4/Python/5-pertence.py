# Recebe uma lista e um valor x e verifica se x está contido na lista

def pertence(n, xs):
    for x in xs:
        if(x == n):
            return True
    return False

print(pertence (1, []) == False) #True
print(pertence (1, [3]) == False) #True
print(pertence (3, [4]) == False) #True
print(pertence (1, [3,7,4,2]) == False) #True
print(pertence (2, [3,7,4,2]) == True) #True
print(pertence (3, [3,7,4,2]) == True) #True
print(pertence (7, [3,7,4,2]) == True) #True