-- Recebe um número inteiro positivo e retorna True se for um 
-- quadrado perfeito e Falso caso contrário

quadperfList n = [x | x <- [1..n], x * x == n] -- Se for quadrado perfeito a lista não vai ser nula

quadperf n = if not $ null $ quadperfList n then True else False

main = do
    a <- readLn :: IO Int
    print $ quadperf a