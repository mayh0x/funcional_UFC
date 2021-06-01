-- Recebe uma lista e retorna o corpo da lista (tudo menos o último elemento)
corpo xs = take (length xs - 1) xs

main = do
    a <- readLn :: IO [Int]
    print $ corpo a