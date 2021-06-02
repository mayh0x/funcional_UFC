-- Recebe uma lista de booleanos e se o total de Trues for ímpar
-- é retornado True, se não, é retornado False

-- Verifica quantos Trues existem na lista
contagemTrue xs = length (filter(\x -> x == True) xs)

paridade [] = False
paridade xs
    | impar xs = True
    | otherwise = False
    where
        impar xs = (contagemTrue xs) `mod` 2 /= 0

main = do
    a <- readLn :: IO [Bool]
    print $ paridade a