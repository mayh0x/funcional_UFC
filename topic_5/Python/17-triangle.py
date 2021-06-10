# Retorna uma lista com as linhas de um triângulo aritmético até n

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

def triangle(n):
    lista = []
    aux = 1
    while(aux <= n):
        lista.append(line(aux))
        aux += 1
    return lista
    
print(triangle(0) == []) #True
print(triangle(1) == [[1]]) #True
print(triangle(2) == [[1], [2,3]]) #True
print(triangle(3) == [[1], [2,3], [4,5,6]]) #True