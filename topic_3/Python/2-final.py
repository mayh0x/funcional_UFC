# Retorne os x números finais da lista

def final(n, xs):
    listafinal = []
    tamlista = len(xs)
    n = tamlista - n
    for x in xs:
        if n < tamlista:
            if x == xs[n]:
                listafinal.append(x)
                n += 1
    return listafinal

print(final (3, [2,5,4,7,9,6]) == [7,9,6]) #True
print(final (2, [2,5,4,7,9,6]) == [9,6]) #True
print(final (1, [2,5,4,7,9,6]) == [6]) #True