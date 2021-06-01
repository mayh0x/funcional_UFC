# Recebe dois números e retorna o menor valor entre eles

def min2(a, b):
    if a < b:
        return a
    else:
        return b

print(min2 (3, 4) == 3) #True
print(min2 (4, 1) == 1) #True
print(min2 (2, 2) == 2) #True
print(min2 (4, -1) == -1) #True