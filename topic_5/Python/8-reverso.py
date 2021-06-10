# Recebe uma lista e retorna a lista na ordem inversa

def reverso(xs):
    return xs[::-1]

print(reverso([]) == []) #True
print(reverso([7]) == [7]) #True
print(reverso([2,3]) == [3,2]) #True
print(reverso([1,2,3,4]) == [4,3,2,1]) #True