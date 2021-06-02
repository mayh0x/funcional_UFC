# Troca dois elementos de uma lista passando a lista e as posições
# a serem trocadas

def swap(xs, a, b):
    if xs != [] and len(xs) > 1: # verifica se a lista é vazia ou se só tem um elemento
        xs[a], xs[b] = xs[b], xs[a]
    return xs

print(swap ([], 0, 5) == []) #True
print(swap ([1], 0, 3) == [1]) #True
print(swap ([1,3,4], 1, 2) == [1,4,3]) #True
print(swap ([1,2,3,4,5,6], 2, 5) == [1,2,6,4,5,3]) #True
print(swap ([5,6,7,8,9], 0, 3) == [8,6,7,5,9]) #True