# Recebe uma lista e retorna o corpo da lista (tudo menos o último elemento)

def corpo(xs):
    corpo = []
    for x in xs:
        if x != xs[-1]:
            corpo.append(x)
    return corpo

print(corpo ([1]) == []) #True
print(corpo ([1,2]) == [1]) #True
print(corpo ([1,2,3,4]) == [1,2,3]) #True