# Retorne quantos números dos 3 são iguais

def iguais(a, b, c):
    cont = 0
    if(a == b and b == c):
        return 3
    elif(a == b or a == c or b == c):
        return 2
    else:
        return 0

print(iguais (2, 2, 2) == 3) #True
print(iguais (2, 2, 3) == 2) #True
print(iguais (2, 3, 2) == 2) #True
print(iguais (2, 1, 1) == 2) #True
print(iguais (3, 2, 1) == 0) #True