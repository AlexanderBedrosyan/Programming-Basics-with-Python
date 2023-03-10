n = int(input())

counter = 0
all_exam_grades = 0

while True:
    name = input()
    if name == "Finish":
        break

    counter += 1
    total_grades = 0

    for i in range(1, n + 1):
        grades = float(input())
        total_grades += grades
        all_exam_grades += grades

    print(f"{name} - {total_grades / n:.2f}.")

print(f"Student's final assessment is {all_exam_grades / (counter * n):.2f}.")
