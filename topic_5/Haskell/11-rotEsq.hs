-- Recebe uma strig e retorna essa lista rotacionada n vezes à esquerda

rotEsq 0 x = x
rotEsq n x = rotEsq (n-1) esq
    where
        esq = tail x ++ [head x]

main = do
    a <- readLn :: IO Int
    b <- getLine
    print $ rotEsq a b