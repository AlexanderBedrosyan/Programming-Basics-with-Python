sum_prime = 0
sum_non_prime = 0

while True:
    n = input()
    if n == "stop":
        break
    else:
        number = int(n)
        if number < 0:
            print("Number is negative.")
            continue

    if number == 2 or number == 3:
        sum_prime += number
    elif number % 2 == 0 or number % 3 == 0:
        sum_non_prime += number
    else:
        sum_prime += number

print(f"Sum of all prime numbers is: {sum_prime}\nSum of all non prime numbers is: {sum_non_prime}")
