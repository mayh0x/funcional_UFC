-- Recebe uma string e retorna a string toda maiúscula

upper_ ' ' = ' '
upper_ char
    | eh_num char == [] = head [grande | (pequeno,grande) <- tup, pequeno == char || grande == char]
    | otherwise = char
    where
      tup = zip ['a'..'z'] ['A'..'Z']
      numeros = ['0'..'9']
      eh_num n = [a | a <- numeros, n == a]
      

upper s = map upper_ s

main = do
    a <- getLine
    print $ upper a