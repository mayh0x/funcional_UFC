-- Recebe uma lista e um valor x e verifica se x só ocorre uma vez, retorna True,
-- se não, retorna False

unico n xs = if num == 1 then True else False
    where
        num = sum (map (\x -> 1) (filter (\x -> n == x) xs))

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO [Int]
    print $ unico a b