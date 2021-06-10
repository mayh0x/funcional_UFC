# recebe um inteiro positivo n e retorna o N-ésimo termo da sequência de fibonacci

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib (n - 2)

print(fib(0) == 0) #True
print(fib(1) == 1) #True
print(fib(2) == 1) #True
print(fib(3) == 2) #True
print(fib(4) == 3) #True
print(fib(5) == 5) #True
print(fib(6) == 8) #True
print(fib(7) == 13) #True