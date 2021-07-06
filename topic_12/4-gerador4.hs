import Data.List

-- gerador4 n = reverse (filter(\x -> x /= 0) [verify n x | x <- list n])
--        where
--           list n = takeWhile (< n+1) (iterate (+1) 0)
--            listverify e = unfoldr (\b -> if b == 0 then Nothing else Just (b, b `div` 2)) e
--            verify e n = if n `elem` listverify e then n else 0

gerador4 elem = takeWhile (\n -> n > 0) $ iterate (\x -> x `div` 2) elem