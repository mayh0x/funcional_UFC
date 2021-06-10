-- Retorna uma lista com as linhas de um triângulo aritmético até n

line 0 = []
line n = [primeiro_elem (n - 1) + 1..primeiro_elem n]
    where
        primeiro_elem n = sum [1..n]

triangle 0 = []
triangle n = [line x | x <- [1..n]]

main = do
    a <- readLn :: IO Int
    print $ triangle a