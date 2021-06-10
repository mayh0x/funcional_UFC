-- Recebe duas listas e retorna uma lista com os elementos intercalados

intercal xs [] = xs
intercal [] ys = ys
intercal (x:xs) (y:ys) = [x] ++ [y] ++ intercal xs ys

main = do
    a <- readLn :: IO [Int]
    b <- readLn :: IO [Int]
    print $ intercal a b