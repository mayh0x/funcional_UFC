-- Recebe uma string S e retorna uma versão de S contendo todos 
-- os caracteres em caixa baixa exceto aqueles que, por serem iniciais 
-- de palavras devem aparecer em caixa alta

upper char = head [grande | (pequeno,grande) <- tup, pequeno == char || grande == char]
    where
      tup = zip ['a'..'z'] ['A'..'Z']

-- lower char = head [pequeno | (pequeno,grande) <- tup, pequeno == char || grande == char]
--    where
--      tup = zip ['a'..'z'] ['A'..'Z']

lower x = if x >= 'A' && x <= 'Z' then toEnum (fromEnum x + 32) else x

titulo_ (c:[]) = []
titulo_ (c:cs) = (if c == ' ' then upper (head cs) else lower (head cs)) : titulo_ cs

titulo s = titulo_ (' ':s)

main = do
    a <- getLine
    print $ titulo a