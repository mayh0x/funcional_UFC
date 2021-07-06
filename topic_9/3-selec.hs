-- Recebe uma lista U e uma listas de posições P, e retorna
-- a lista das chaves de U cujas posições estão em P

selec " " _ = " "
selec xs ys = [xs !! p | p <- ys]

main = do
    a <- getLine
    b <- readLn :: IO [Int]
    print $ selec a b