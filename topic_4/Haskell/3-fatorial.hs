-- Faz o fatorial de um número x
fatorial x
    | x == 0 || x == 1 = 1
    | otherwise = x * fatorial (x - 1)

main = do
    a <- readLn :: IO Int
    print $ fatorial a