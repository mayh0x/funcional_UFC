# Calcular a soma de 1 até n que são múltiplos de 3 ou 5

def euler1(n):
    lista = []
    soma = 0
    valor = 1
    for r in range(n): #faz uma repetição até o valor final (n)
        if valor < n:
            lista.append(valor)
            valor += 1
    
    for i in lista:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            soma += int(i)
    return soma

print(euler1 (3) == 0) #True
print(euler1 (4) == 3) #True
print(euler1 (5) == 3) #True
print(euler1 (6) == 8) #True
print(euler1 (10) == 23) #True
print(euler1 (1000) == 233168) #True