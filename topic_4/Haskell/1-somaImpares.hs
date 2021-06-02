-- Soma todos os números ímpares de uma lista
somaImpares xs = sum (filter (\x -> x `mod` 2 /= 0) xs)

main = do
    a <- readLn :: IO [Int]
    print $ somaImpares a