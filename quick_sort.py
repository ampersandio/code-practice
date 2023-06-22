x = [1,45,6,8,0,2,3,7,23,678,12]

def quicksort(lst):
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
    

    return(quicksort(left) + [pivot] + quicksort(right))


print(quicksort(x))