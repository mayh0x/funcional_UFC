-- Recebe um numero n e uma lista e retorna os n menores elementos
-- da lista na ordem que aparecem na lista

menores 0 xs = []
menores n xs
    | length xs == n = xs
    | minimum xs == maximum xs = [(length xs-n)..(length xs)]
    | otherwise = menores n (filter (/= maximum xs) xs)

main = do
    a <- readLn :: IO Int
    b <- readLn :: IO [Int]
    print $ menores a b