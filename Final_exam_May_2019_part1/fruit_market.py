strawberries_price = float(input())
bananas_kg = float(input())
orange_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_total = (0.50 * strawberries_price) * raspberries_kg
orange_total = (0.60 * (0.50 * strawberries_price)) * orange_kg
bananas_total = (0.20 * (0.50 * strawberries_price)) * bananas_kg

total = raspberries_total + orange_total + bananas_total + strawberries_kg * strawberries_price

print(total)
