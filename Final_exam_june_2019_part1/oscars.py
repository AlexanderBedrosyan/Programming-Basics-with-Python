name = input()
academy_points = float(input())
lectors = int(input())

needed_points = 1250.5
total_points = academy_points

for i in range(1, lectors + 1):
    teacher = input()
    teacher_points = float(input())

    total_points += ((len(teacher) * teacher_points) / 2)

    if total_points >= needed_points:
        print(f"Congratulations, {name} got a nominee for leading role with {total_points:.1f}!")
        exit()

print(f"Sorry, {name} you need {needed_points - total_points:.1f} more!")
