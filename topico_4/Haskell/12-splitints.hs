-- Recebe uma lista e retorna uma tupla com uma lista de ímpares
-- e outra lista de pares

-- pega so os numeros impares
splitimpar xs = [x | x <- xs, impar x]
    where
        impar x = x `mod` 2 /= 0

-- pega so os numeros pares
splitpar xs = [x | x <- xs, par x]
    where
        par x = x `mod` 2 == 0

-- tamanho da lista de impares
tamimpar xs = length(splitimpar xs)

-- Retorna a tupla das listas de impares e pares juntas
splitints xs = splitAt (tamimpar xs) (juntarlistas (splitimpar xs) (splitpar xs))
    where
        juntarlistas xs ys = xs ++ ys

main = do
    a <- readLn :: IO [Int]
    print $ splitints a