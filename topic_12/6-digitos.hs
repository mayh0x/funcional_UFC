import Data.List

digitos num = reverse (unfoldr condition num)
    where
        condition x | x == 0 = Nothing 
                    | otherwise = Just (x `mod` 10, x `div` 10)