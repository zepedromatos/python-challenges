# Find the largest prime factor

number = 600851475143
i = 2
while number > 1:
    while number % i == 0:
        number = int(number/i)
    i += 1
else:
    print(i-1)
