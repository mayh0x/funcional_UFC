# Recebe três números e retorna o maior valor entre eles

def max3(a, b, c):
    if(a > b):
        if(a > c):
            return a
        else:
            return c
    else:
        if(b > c):
            return b
        else:
            return c

print(max3 (6, 2, 4) == 6) #True
print(max3 (6, 7, 4) == 7) #True
print(max3 (6, 7, 9) == 9) #True
print(max3 (5, 2, 5) == 5) #True