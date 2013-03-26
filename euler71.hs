import Data.Ratio
import Data.List
import Data.Maybe(fromJust)

lowerbound = floor $ 3 / 7 * (10 ^6) - 100
upperbound = lowerbound + 200

ratiolist  =  sort $ nub[( a % b) | b <- [999990..1000000], a <- [lowerbound..upperbound], a < b,(a % b) <= (3 % 7)]

index = (fromJust $ elemIndex (3 % 7) ratiolist) - 1

result = numerator $ ratiolist !! index

main = print result

