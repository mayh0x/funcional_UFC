-- Recebe uma lista e retorna o total de elementos da lista
total xs = sum (map (\x -> 1) xs)

main = do
    a <- readLn :: IO [Int]
    print $ total a