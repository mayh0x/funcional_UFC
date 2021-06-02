-- Recebe uma lista e um valor x e verifica se x está contido na lista
pertence x xs = elem x xs

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO [Int]
    print $ pertence a b