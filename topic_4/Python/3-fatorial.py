# Faz o fatorial de um número x

def fatorial(num):
    resultado = 1
    if(num == 0 or num == 1):
        return 1
    
    for n in range(1, (num+1)):
        resultado = resultado * n
    
    return resultado

print(fatorial(0) == 1) #True
print(fatorial(1) == 1) #True
print(fatorial(5) == 120) #True