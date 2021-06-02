-- Recebe dois números e retorna o menor valor entre eles
min2 x y
    | x < y = x
    | otherwise = y

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    print $ min2 a b