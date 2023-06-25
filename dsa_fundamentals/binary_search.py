def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return "Not Found"


def binary_search2(lst, n):
    length = len(lst)
    index = length // 2

    while index >= 0:
        if lst[index] == n:
            return index
        
        elif lst[index] > n:
            index = (index - 1) // 2
        else:
            index = (index + 1 + length) // 2



lst = [1, 3, 4, 4.5, 5, 11, 13]
print(binary_search(lst, 5))


