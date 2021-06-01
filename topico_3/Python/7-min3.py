# Recebe três números e retorna o menor valor entre eles

def min3(a, b, c):
    if(a < b):
        if(a < c):
            return a
        else:
            return c
    else:
        if(b < c):
            return b
        else:
            return c

print(min3 (1, 2, 3) == 1) #True
print(min3 (2, 1, 3) == 1) #True
print(min3 (3, 4, 2) == 2) #True
print(min3 (2, 5, 4) == 2) #True