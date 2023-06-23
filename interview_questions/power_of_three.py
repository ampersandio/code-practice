def power_of_three(n):
    if n == 1:
        return True

    return power_of_three(n//3) if n % 3 == 0 else False


print(power_of_three(6))

def power_of_three_iterative(n):
    while n % 3 == 0:
        n = n //3

    return n == 1
    

print(power_of_three_iterative(6))