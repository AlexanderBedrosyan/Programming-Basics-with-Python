goal = int(input())

starting_point = goal - 30
counter = 0
all_jumps = 0

while True:
    jump = int(input())
    all_jumps += 1

    if jump > starting_point:
        starting_point += 5
        counter = 0
        if starting_point > goal:
            print(f"Tihomir succeeded, he jumped over {goal}cm after {all_jumps} jumps.")
            break
    else:
        counter += 1

    if counter == 3:
        print(f"Tihomir failed at {starting_point}cm after {all_jumps} jumps.")
        break
