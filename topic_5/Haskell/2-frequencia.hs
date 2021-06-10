-- Recebe uma lista e um valor n e retorna o total de ocorrências de x

frequencia n [] = 0
frequencia n xs = sum (map (\x -> 1) (filter (\x -> n == x) xs))

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO [Int]
    print $ frequencia a b