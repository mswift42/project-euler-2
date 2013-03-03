
length_number :: Integer -> Int
length_number n = length $ show n

power_digit = [(x,y) | x <- [1..1000], y <- [1..100], (length_number(x^y)==y)]

main = do
  print (length power_digit)
