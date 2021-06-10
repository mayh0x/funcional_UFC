# Recebe um numero n e uma lista e retorna os n menores elementos
# da lista na ordem que aparecem na lista

def menores(n, xs):
    if len(xs) == n:
        return xs
    
    if min(xs) == max(xs):
        return xs[len(xs)-n:len(xs)]
    else:
        return menores(n, [x for x in xs if x != max(xs)])

print(menores(0, [6,2,2,4,9]) == []) #True
print(menores(1, [6,2,2,4,9]) == [2]) #True
print(menores(3, [5,5,5]) == [5,5,5]) #True
print(menores(1, [5,5,5]) == [5]) #True
print(menores(3, [6,2,3,4,9]) == [2,3,4]) #True
print(menores(3, [5,3,1,9,7,2]) == [3,1,2]) #True