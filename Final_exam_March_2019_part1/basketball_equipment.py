tax = int(input())

sneakers = tax * 0.60
equipment = sneakers * 0.80
ball = equipment / 4
accessoirs = ball / 5
total_sum = sneakers + tax + equipment + ball + accessoirs

print(f"{total_sum:.2f}")
