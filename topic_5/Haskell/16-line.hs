-- Retorna uma linha do triângulo aritmético

line 0 = []
line n = [primeiro_elem (n - 1) + 1..primeiro_elem n]
    where
        primeiro_elem n = sum [1..n]

main = do
    a <- readLn :: IO Int
    print $ line a