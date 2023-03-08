player = input()

starting_points = 301
shots = 0
unsuccessful_shots = 0

while True:
    type_shot = input()
    if type_shot == "Retire":
        print(f"{player} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    points = int(input())
    shots += 1

    if type_shot == "Double":
        points = 2 * points
        starting_points -= points
    elif type_shot == "Triple":
        points = 3 * points
        starting_points -= points
    else:
        starting_points -= points

    if starting_points < 0:
        starting_points += points
        unsuccessful_shots += 1
    elif starting_points == 0:
        print(f"{player} won the leg with {shots - unsuccessful_shots} shots.")
        break
