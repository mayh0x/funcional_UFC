# Recebe um número inteiro positivo e retorna True se for um 
# quadrado perfeito e Falso caso contrário

def quadperf(n):
    raiz = int(n ** (1/2))
    if (raiz ** 2) == n:
        return True
    return False

print(quadperf(12) == False) #True
print(quadperf(16) == True) #True
print(quadperf(25) == True) #True
print(quadperf(5) == False) #True