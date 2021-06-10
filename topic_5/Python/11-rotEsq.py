# Recebe uma strig e retorna essa lista rotacionada n vezes à esquerda

def rotEsq(n, x):
    if n == 0:
        return x
    comeco = x[0]
    resto = x[1:]
    esq = resto + comeco
    return rotEsq((n - 1), esq)

print(rotEsq(0, "asdfg") == "asdfg") #True
print(rotEsq(1, "asdfg") == "sdfga") #True
print(rotEsq(3, "asdfg") == "fgasd") #True
print(rotEsq(4, "asdfg") == "gasdf") #True