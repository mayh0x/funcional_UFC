import Data.List

gerador1 = iterate condition 0
    where
      condition x = if x > 0 then -x else 1-x