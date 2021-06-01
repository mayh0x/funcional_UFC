-- Recebe três números e retorna o maior valor entre eles
max3 a b c
    | a > b && a > c = a
    | a > b && a < c = c
    | b > c && a < b = b
    | otherwise = c

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    c <- readLn :: IO Int
    print $ max3 a b c