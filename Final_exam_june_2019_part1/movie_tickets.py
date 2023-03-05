a1 = int(input())
a2 = int(input())
n = int(input())

num1 = ""
num2 = 0
num3 = 0
num4 = 0

result = []

for i in range(a1, a2):
    for l in range(1, n):
        for z in range(1, n // 2):
            for a in range(a1, a2):
                if i % 2 != 0:
                    num1 = chr(i)
                else:
                    continue
                if a % 2 != 0:
                    num4 = i
                else:
                    continue
                if (l + z + a) % 2 != 0:
                    num2 = l
                    num3 = z
                else:
                    continue

                if f"{num1}-{num2}{num3}{num4}" in result:
                    continue

                result.append(f"{num1}-{num2}{num3}{num4}")

for item in range(0, len(result)):
    print(result[item])
