# Recebe uma lista e um valor x e verifica se x só ocorre uma vez, retorna True,
# se não, retorna False

def unico(n, xs):
    cont = 0
    for x in xs:
        if x == n:
            cont += 1
    if(cont == 1):
        return True
    return False

print(unico(2, [2]) == True) #True
print(unico(2, [3,1]) == False) #True
print(unico(2, [1,2,3,2]) == False) #True