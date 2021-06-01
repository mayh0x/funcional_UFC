-- Recebe duas listas e retorna a intercessão entre elas
elemento x [] = False -- retorna se um elemento está na lista
elemento x (y:ys) 
    | x == y = True
    | otherwise = elemento x ys

intersec [] [] = []
intersec xs [] = []
intersec [] xs = []
intersec xs ys = [x | x <- xs, elemento x ys]

-- Também posso fazer assim:
-- intersec (x:xs) ys = if(elemento x ys) then x : intersec xs ys else intersec xs ys

main = do
    a <- readLn :: IO [Int]
    b <- readLn :: IO [Int]
    print $ intersec a b