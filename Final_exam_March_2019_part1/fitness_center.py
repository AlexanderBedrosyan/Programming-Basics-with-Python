n = int(input())

list1 = ["Back", "Chest", "Legs", "Abs"]

back = 0
chest = 0
legs = 0
abs = 0
training_people = 0

protein_shake = 0
protein_bar = 0
eating = 0

for i in range(1, n + 1):
    type_acts = input()

    if type_acts in list1:
        training_people += 1
        if type_acts == "Back":
            back += 1
        elif type_acts == "Chest":
            chest += 1
        elif type_acts == "Legs":
            legs += 1
        elif type_acts == "Abs":
            abs += 1
    else:
        eating += 1
        if type_acts == "Protein shake":
            protein_shake += 1
        elif type_acts == "Protein bar":
            protein_bar += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{(training_people / (eating + training_people)) * 100:.2f}% - work out")
print(f"{(eating / (training_people + eating)) * 100:.2f}% - protein")
