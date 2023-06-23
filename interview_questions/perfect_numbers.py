'''
Perfect Number

A perfect number is a positive integer that is equal to the sum of its proper positive divisors, 
that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). 
Equivalently, a perfect number is a number that is half the sum of all its positive divisors (including itself). 
Write a method that prints the first 4 perfect numbers.

Perfect Number Example

6 = 1 + 2 + 3

'''

from math import sqrt, ceil

'''
You can find the divisors of an integer by only traversing to the sqrt of this number!!! 
'''

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

print(*perfect_numbers)