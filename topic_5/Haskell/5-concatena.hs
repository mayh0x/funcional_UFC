-- Recebe duas listas e retorna a concatenação delas

concatena [] [] = []
concatena xs [] = xs
concatena [] ys = ys
concatena xs ys = xs ++ ys

main = do
    a <- readLn :: IO [Int]
    b <- readLn :: IO [Int]
    print $ concatena a b