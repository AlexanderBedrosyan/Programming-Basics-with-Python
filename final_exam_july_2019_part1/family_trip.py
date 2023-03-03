family_budget = float(input())
nights = int(input())
night_price = float(input())
percent_additional_expenses = int(input())

nights_amount = nights * night_price
discount_nights_amount = (night_price - (night_price * 5 / 100)) * nights

percent_additional_expenses = family_budget * percent_additional_expenses / 100

total_amount = nights_amount + percent_additional_expenses
total_discount_amount = discount_nights_amount + percent_additional_expenses

if nights > 7 and total_discount_amount <= family_budget:
    left_amount = family_budget - total_discount_amount
    print(f"Ivanovi will be left with {left_amount:.2f} leva after vacation.")

elif nights > 7 and total_discount_amount > family_budget:
    needed_amount = total_discount_amount - family_budget
    print(f"{needed_amount:.2f} leva needed.")

elif nights <= 7 and total_amount <= family_budget:
    left_amount = family_budget - total_amount
    print(f"Ivanovi will be left with {left_amount:.2f} leva after vacation.")

elif nights <= 7 and total_amount > family_budget:
    needed_amount = total_amount - family_budget
    print(f"{needed_amount:.2f} leva needed.")
