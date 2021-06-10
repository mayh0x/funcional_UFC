# Retorna uma linha do triângulo aritmético

def line(n):
    if n == 0:
        return []
    aux = 1
    lista_aux = []
    while(aux < n):
        lista_aux.append(aux)
        aux += 1
    lista = []
    lista.append(sum(lista_aux) + 1)

    cont = 1
    while(cont < n):
        lista.append((int(lista[cont-1]) + 1))
        cont += 1
    
    return lista

print(line(0) == []) #True
print(line(1) == [1]) #True
print(line(2) == [2,3]) #True
print(line(3) == [4,5,6]) #True