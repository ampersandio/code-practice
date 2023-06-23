lst = [1,4,5,7,9,2,23,3,67,8,]

'''
Bubble Sort
time complexity - O(n^2)
space complexity - O(1)

'''

def bubble_sort(lst):
    length = len(lst)-1
    
    for _ in range(length):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1], lst[i]
        length -= 1

    return lst

# print(bubble_sort(lst))


def bubble_sort(lst):
    length = len(lst)-1
    
    for _ in range(length):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
        length -= 1

    return lst

print(bubble_sort(lst))