-- Retorna uma sublista passando o inicio, o fim e uma lista na qual
-- será retirada a sublista

sublist a b xs = drop inicio (take fim xs)
    where
        inicio = if a < 0 then a + (length xs) else a
        fim = if b < 0 then b + (length xs) else b

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    c <- readLn :: IO [Int]
    print $ sublist a b c