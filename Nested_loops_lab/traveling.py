counter = 0
destination_name = ""
traveling_sum = 0
saving_amount = 0

while True:
    n = input()
    if n == "End":
        break
    counter += 1
    if counter == 1:
        destination_name = n
    elif counter == 2:
        traveling_sum = n
    elif counter > 2:
        saving_amount += float(n)

    if (float(saving_amount) >= float(traveling_sum)) and (counter > 2):
        print(f"Going to {destination_name}!")
        destination_name = ""
        traveling_sum = 0
        saving_amount = 0
        counter = 0
