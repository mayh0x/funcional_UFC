-- Recebe uma lista e um número n e retorna uma tupla de listas
-- onde a tupla 1 é formada pelos primeiros n elementos da lista
-- e a tupla 2 formada pelo restante

divide xs x = splitAt x xs 

main = do
    a <- readLn :: IO [Int]
    b <- readLn :: IO Int
    print $ divide a b