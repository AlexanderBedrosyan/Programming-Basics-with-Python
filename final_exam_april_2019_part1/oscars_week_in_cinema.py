movie_name = input()
type_of_room = input().lower()
number_of_tickets = int(input())

list_amounts = []
ticket_price = 0

if movie_name == "A Star Is Born":
    list_amounts = [7.50, 10.50, 13.50]
elif movie_name == "Bohemian Rhapsody":
    list_amounts = [7.35, 9.45, 12.75]
elif movie_name == "Green Book":
    list_amounts = [8.15, 10.25, 13.25]
else:
    list_amounts = [8.75, 11.55, 13.95]

if type_of_room == "normal":
    ticket_price = list_amounts[0]
elif type_of_room == "luxury":
    ticket_price = list_amounts[1]
elif type_of_room == "ultra luxury":
    ticket_price = list_amounts[2]

total_amount = ticket_price * number_of_tickets

print(f"{movie_name} -> {total_amount:.2f} lv.")
