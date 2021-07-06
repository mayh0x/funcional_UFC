-- Recebe uma lista e retorna a lista dos segmentos iniciais,
-- os mais curtos no fim

tails [x] = [[x], []]
tails (x:xs) = (x:xs) : tails(xs)

main = do
    a <- readLn :: IO [Int]
    print $ tails a