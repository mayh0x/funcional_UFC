-- Recebe uma string e retorna True se é palíndromo, se não, retorna False

isPalind s
    | s == invertido = True
    | otherwise = False
    where
        invertido = reverse s

main = do
    a <- getLine
    print $ isPalind a