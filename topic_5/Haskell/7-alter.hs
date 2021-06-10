-- Recebe um inteiro e os números até ele (com os negativos desses numeros)

alter 1 = [1, -1]
alter n = alter (n - 1) ++ valores
    where
        valores = [n, -n]

main = do
    a <- readLn :: IO Int
    print $ alter a