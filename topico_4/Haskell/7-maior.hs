-- Recebe uma lista e retorna o maior valor da lista
maior [x] = x
maior (x:xs)
    | maior xs < x = x
    | otherwise = maior xs

main = do
    a <- readLn :: IO [Int]
    print $ maior a