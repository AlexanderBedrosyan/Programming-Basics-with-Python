movie = input()
ticket_type = input()
tickets = int(input())

drink_price = [12, 18, 9]
pop_price = [15, 25, 11]
menu_price = [19, 30, 14]

ticket_amount = 0

if movie == "John Wick":
    if ticket_type == "Drink":
        ticket_amount = drink_price[0]
    elif ticket_type == "Popcorn":
        ticket_amount = pop_price[0]
    else:
        ticket_amount = menu_price[0]
elif movie == "Star Wars":
    if ticket_type == "Drink":
        ticket_amount = drink_price[1]
    elif ticket_type == "Popcorn":
        ticket_amount = pop_price[1]
    else:
        ticket_amount = menu_price[1]
else:
    if ticket_type == "Drink":
        ticket_amount = drink_price[2]
    elif ticket_type == "Popcorn":
        ticket_amount = pop_price[2]
    else:
        ticket_amount = menu_price[2]

if movie == "Jumanji" and tickets == 2:
    ticket_amount *= 0.85
elif movie == "Star Wars" and tickets >= 4:
    ticket_amount *= 0.70

print(f"Your bill is {ticket_amount * tickets:.2f} leva.")
