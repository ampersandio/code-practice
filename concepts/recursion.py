# Recursive Palindrome

def rec_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
        return rec_palindrome(s[1:-1])
    else:
        return False
    
# print(rec_palindrome("aasbaa"))


# Reverse String

def rec_reverse(s:str) -> str:
    if len(s) == 1:
        return s
    
    return s[-1] + rec_reverse(s[:-1])


# Fibonacci 

def rec_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fibonacci(n - 1) + rec_fibonacci(n - 2)

# print(rec_fibonacci(10))

# Factorial

def rec_factorial(n):
    if n == 1:
        return 1
    return n * rec_factorial(n-1)

# print(rec_factorial(5))

# Quick Sort 

def quick_sort(lst:list[int]) -> int:
    if len(lst) <= 1:
        return lst
    
    pivot = lst[-1]

    left = []
    right = []


    for i in lst[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([23,36,7,8,9,2234,5,67]))

