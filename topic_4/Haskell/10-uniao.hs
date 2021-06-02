-- Recebe duas listas e retorna a união entre elas
elemento x [] = False -- retorna se um elemento está na lista
elemento x (y:ys) 
    | x == y = True
    | otherwise = elemento x ys

uniao [] [] = []
uniao [] xs = xs
uniao xs [] = xs
-- uniao em ordem
--uniao (x:xs) (y:ys)
--    | x < y = x : uniao xs (y:ys)
--    | x > y = y : uniao (x:xs) ys
--    | otherwise = x : uniao xs ys
--
-- uniao sem ser em ordem
uniao xs ys = xs ++ [y | y <- ys, not (elemento y xs)]

main = do
    a <- readLn :: IO [Int]
    b <- readLn :: IO [Int]
    print $ uniao a b