from math import sqrt, ceil

def find_divisors(n):
    divisors = 0
    for i in range(1,ceil(sqrt(n))):
        if n % i == 0:
            divisors += i
            divisors += n // i

    return divisors-n == n

perfect_numbers = []
count = 1

while len(perfect_numbers) < 4:
    if find_divisors(count):
        perfect_numbers.append(count)

    count += 1

print(perfect_numbers)