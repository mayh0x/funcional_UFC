-- Conte os números negativos de uma lista

-- do jeito que eu pensei sem filter
listaNegativa xs = [x | x<-xs, x < 0]
countNeg xs = length (listaNegativa xs)

-- com filter
-- countNeg xs = length (filter(\x -> x < 0) xs)

main = do
    a <- readLn :: IO [Int]
    print $ countNeg a