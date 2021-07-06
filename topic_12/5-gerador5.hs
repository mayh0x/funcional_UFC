import Data.List

gerador5 n = unfoldr condition n
    where
        condition x | x == 0 = Nothing
                    | otherwise = Just (x, x `div` 2)