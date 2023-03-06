nights = 20
transport = 1.60
ticket_museum = 6

people = int(input())
count_nights = int(input())
count_transports = int(input())
count_tickets = int(input())

price_without_adding = count_nights * nights + count_transports * transport + count_tickets * ticket_museum
total_price = people * price_without_adding
final_price = total_price * 1.25

print(f"{final_price:.2f}")
