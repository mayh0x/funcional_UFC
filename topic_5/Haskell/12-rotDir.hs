-- Recebe uma strig e retorna essa lista rotacionada n vezes à direita

rotDir 0 x = x
rotDir n x = rotDir (n-1) dir
    where
        size = length x
        tira_ultimo = reverse (tail (reverse x))
        pega_ultimo = drop (size - 1) x
        dir = pega_ultimo ++ tira_ultimo