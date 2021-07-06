-- produtoEscalar [1,2,3] [4,5,6]
-- (1 * 4) + (2 * 5) + (3 * 6) => 32
-- OBS: Fazer com zip

produtoEscalar xs ys = total ([x*y | (x,y) <- zip xs ys])
    where
        total [] = 0
        total (l:ls) = l + total ls

main = do
    a <- readLn :: IO [Int]
    b <- readLn :: IO [Int]
    print $ produtoEscalar a b