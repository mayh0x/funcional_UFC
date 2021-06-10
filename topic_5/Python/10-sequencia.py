# Recebe dois numeros n e m e retorna uma lista [m, m+1, m+2, ..., m+n-1]

def sequencia(n, m):
    if n == 0:
        return []
    return [m] + sequencia((n - 1), (m + 1))

print(sequencia(0, 2) == []) #True
print(sequencia(1, 2) == [2]) #True
print(sequencia(3, 5) == [5,6,7]) #True
print(sequencia(4, 4) == [4,5,6,7]) #True