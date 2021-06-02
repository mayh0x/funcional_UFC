-- Recebe três números e retorna o menor valor entre eles
min3 a b c
    | a < b && a < c = a
    | a < b && a > c = c
    | b < c && a > b = b
    | otherwise = c
    

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    c <- readLn :: IO Int
    print $ min3 a b c