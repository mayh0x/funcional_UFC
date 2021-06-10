-- Recebe um numero n e uma lista e retorna uma sublista de numeros que
-- são maiores que n da lista

maioresQue n [] = []
maioresQue n xs = filter (> n) xs

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO [Int]
    print $ maioresQue a b