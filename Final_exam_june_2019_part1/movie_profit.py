movie = input()
days = int(input())
tickets = int(input())
price = float(input())
cinema_percent = int(input())

day_count = tickets * price
total_days_count = day_count * days
cinema_price = total_days_count * (cinema_percent / 100)

total_amount = total_days_count - cinema_price

print(f"The profit from the movie {movie} is {total_amount:.2f} lv.")
