# Recebe uma strig e retorna essa lista rotacionada n vezes à direita

def rotDir(n, x):
    if n == 0:
        return x
    pega_ultimo = x[len(x)-1]
    tira_ultimo = x[:-1]
    dire = pega_ultimo + tira_ultimo
    return rotDir((n - 1), dire)

print(rotDir(0, "asdfg") == "asdfg") #True
print(rotDir(1, "asdfg") == "gasdf") #True
print(rotDir(3, "asdfg") == "dfgas") #True
print(rotDir(4, "asdfg") == "sdfga") #True