import math

numbers_of_people = int(input())
entrance_price = float(input())
sun_lounger_price = float(input())
umbrella_price = float(input())

SUN_LOUNGER_NEEDED = numbers_of_people * 75 / 100
NUMBER_PEOPLE_FOR_UMBRELLA = numbers_of_people / 2

total_price_sun_lounger = sun_lounger_price * math.ceil(SUN_LOUNGER_NEEDED)
total_price_umbrella = math.ceil(NUMBER_PEOPLE_FOR_UMBRELLA) * umbrella_price
total_price_entrance = entrance_price * numbers_of_people

event_price = total_price_entrance + total_price_umbrella + total_price_sun_lounger

print(f"{event_price:.2f} lv.")
