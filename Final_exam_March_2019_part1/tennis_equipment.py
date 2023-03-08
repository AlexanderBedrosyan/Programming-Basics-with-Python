import math

price_tennis_racket = float(input())
n = int(input())
m = int(input())

price_shoes = price_tennis_racket / 6
more_equipments = (price_tennis_racket * n + price_shoes * m) * 0.20
total_amount = (price_tennis_racket * n + price_shoes * m) + more_equipments

print(f"Price to be paid by Djokovic {math.floor(1/8 * total_amount)}\nPrice to be paid by sponsors {math.ceil(7/8 * total_amount)}")
