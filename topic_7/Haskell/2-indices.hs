-- Recebe um numero n e uma lista e retorna as posições onde
-- n aparece na lista

indices n xs = [indice | (indice, elem) <- zip [0..] xs, elem == n]

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO [Int]
    print $ indices a b