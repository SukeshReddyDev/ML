num = int(input("Enter a number: "))

temp = num
sum_fact = 0

while num > 0:

    digit = num % 10

    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    sum_fact = sum_fact + fact

    num = num // 10

if temp == sum_fact:
    print(temp, "is a Strong Number")
else:
    print(temp, "is not a Strong Number")