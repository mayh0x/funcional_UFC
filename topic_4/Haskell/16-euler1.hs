-- Calcular a soma de 1 até n que são múltiplos de 3 ou 5
euler1 n = sum (filter(\x -> div3 x || div5 x) [1..(n-1)])
-- sum [x | x <- [1..(a-1)], div3 x || div5 x]
    where
        div3 x = x `mod` 3 == 0
        div5 x = x `mod` 5 == 0

main = do
    a <- readLn :: IO Int
    print $ euler1 a