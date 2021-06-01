-- Recebe uma lista e um numero n e retorna o n-ésimo termo da lista
elemento n xs
    | n < 0 = xs !! negativoAdaptado
    | otherwise = xs !! n
    where
        negativoAdaptado = n + length xs

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO [Int]
    print $ elemento a b