-- Troca dois elementos de uma lista passando a lista e as posições
-- a serem trocadas

swap [] a b = []
swap [x] a b = [x]
swap xs a b = comeco ++ elemB ++ meio ++ elemA ++ fim
    where
        comeco = take a xs
        elemB = take 1 (drop b xs)
        meio = drop (a+1) (take b xs)
        elemA = take 1 (drop a xs)
        fim = drop (b+1) xs
    
main = do
    a <- readLn :: IO [Int]
    b <- readLn :: IO Int
    c <- readLn :: IO Int
    print $ swap a b c