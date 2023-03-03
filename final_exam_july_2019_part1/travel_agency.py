city = input()
packet = input()
vip_card = input()
days = int(input())

if days > 7:
    days = days - 1

if city == "Bansko" or city == "Borovets":
    price_equipment_food = 100
    price_no_equipment_food = 80
    vip_discount_equipment_food = 0.10
    vip_discount_no_equipment_food = 0.05

elif city == "Burgas" or city == "Varna":
    price_equipment_food = 130
    price_no_equipment_food = 100
    vip_discount_equipment_food = 0.12
    vip_discount_no_equipment_food = 0.07

else:
    print("Invalid input!")
    exit()

if vip_card == "yes" and packet == "withEquipment" or packet == "withBreakfast":
    total_price = (price_equipment_food - (price_equipment_food * vip_discount_equipment_food)) * days

elif vip_card == "no" and packet == "noEquipment" or packet == "noBreakfast":
    total_price = price_no_equipment_food * days

elif vip_card == "yes" and packet == "noEquipment" or packet == "noBreakfast":
    total_price = (price_no_equipment_food - (price_no_equipment_food * vip_discount_no_equipment_food)) * days

elif vip_card == "no" and packet == "withEquipment" or packet == "withBreakfast":
    total_price = price_equipment_food * days

else:
    print("Invalid input!")
    exit()

if days < 1:
    print("Days must be positive number!")
    exit()

print(f"The price is {total_price:.2f}lv! Have a nice time!")
