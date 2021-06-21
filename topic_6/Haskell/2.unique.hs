-- Recebe uma lista com possíveis chaves repetidas e retorna
-- uma lista sem repetições

-- import Data.List

unique [] = []
unique [x] = [x]
unique (x:xs) = [x] ++ unique [y | y <- xs, y /= x]

-- unique xs = Data.List.nub xs

main = do
    a <- readLn :: IO [Int]
    print $ unique a