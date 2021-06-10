-- recebe um inteiro positivo n e retorna o N-ésimo termo da sequência de fibonacci
fib 0 = 0
fib 1 = 1
fib n = fib(n - 1) + fib(n - 2)

main = do
    a <- readLn :: IO Int
    print $ fib a