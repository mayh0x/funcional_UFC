-- Retorna se uma gangorra está equilibrada ou não
-- A função recebe os inteiros P_1, C_1, P_2 e C_2 respectivamente
-- P_1 x C_1 for igual a P_2 x C_2 => 0
-- P_1 x C_1 for maior que P_2 x C_2 => -1
-- P_1 x C_1 for menor que P_2 x C_2 => 1

gangorra a b c d
    | a * b == c * d = 0
    | a * b > c * d = -1
    | otherwise = 1

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    c <- readLn :: IO Int
    d <- readLn :: IO Int
    print $ gangorra a b c d