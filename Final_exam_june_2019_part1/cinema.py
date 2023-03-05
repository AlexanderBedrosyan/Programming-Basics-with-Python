capacity = int(input())

total_vieweres = 0
discount = 0

while True:
    viewers = input()
    if total_vieweres == capacity and viewers != "Movie time!":
        if int(viewers) % 3 == 0:
            discount -= 5
            total_vieweres = capacity

    if viewers == "Movie time!":
        print(f"There are {capacity - total_vieweres} seats left in the cinema.\nCinema income -"
              f" {total_vieweres * 5 - discount} lv.")
        break

    if total_vieweres + int(viewers) > capacity and total_vieweres != capacity:
        print(f"The cinema is full.\nCinema income - {total_vieweres * 5 - discount:} lv.")
        break

    total_vieweres += int(viewers)

    if total_vieweres > capacity:
        if int(viewers) % 3 != 0:
            print(f"The cinema is full.\nCinema income - {capacity * 5 - discount:} lv.")
            break
        elif int(viewers) % 3 == 0:
            discount += 5
            print(f"The cinema is full.\nCinema income - {capacity * 5 - discount:} lv.")
            break

    if viewers != "Movie time!":
        if int(viewers) % 3 == 0:
            discount += 5

    if total_vieweres == capacity:
        continue




# print(f"There are {capacity - total_vieweres} seats left in the cinema.\nCinema income - {total_amount} lv.")

# print(f"The cinema is full.\nCinema income - {capacity * 5 - discounts:} lv.")