-- Recebe dois numeros n e m e retorna uma lista [m, m+1, m+2, ..., m+n-1]

sequencia 0 _ = []
sequencia n m = [m] ++ sequencia (n - 1) (m + 1)

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    print $ sequencia a b