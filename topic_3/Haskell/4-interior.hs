-- Retorne uma lista sem o primeiro nem o último elemento
interior xs = tail(take (length xs - 1) xs)

main = do
    a <- readLn :: IO [Int]
    print $ interior a