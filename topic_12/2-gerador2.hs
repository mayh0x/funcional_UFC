import Data.List

gerador2 = iterate (\x -> if x > 0 then (-x-1) else (-x+1)) 1
    