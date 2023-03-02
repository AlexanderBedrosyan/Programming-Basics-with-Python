movie_budget = float(input())
statists = int(input())
dresses = float(input())

decor = movie_budget * 0.1
dresses_amount = statists * dresses

if statists > 150:
    dresses_amount *= 0.90

amount_needed = dresses_amount + decor

if amount_needed > movie_budget:
    print(f"Not enough money!\nWingard needs {abs(movie_budget - amount_needed):.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {movie_budget - amount_needed:.2f} leva left.")
