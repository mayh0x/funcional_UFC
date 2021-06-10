-- Remove a primeira ocorrência de um número numa lista

deletee x [] = []
deletee n (x:xs)
    | n == x = xs
    | otherwise = [x] ++ deletee n xs

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO [Int]
    print $ deletee a b