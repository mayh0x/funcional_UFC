-- Recebe uma lista e retorna uma versão acumulativa da lista
-- Na versão acumulativa, soma-se as todas as chaves de u até a posição k

listacc [] = []
listacc [x] = [x]
listacc xs = listacc tira_fim ++ [sum xs]
    where
        tira_fim = reverse (tail (reverse xs))