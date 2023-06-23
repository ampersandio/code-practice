x = []
y = [94797]

'''
Space Complexity - O(n) it creates new lists, it's not sorted in place
Time Complexity - O(n log n) dividing (log n) bringing it all back together - n
'''


def merge(lst1,lst2):
    '''
    basic merge function
    '''
    combined = []
    i = 0
    j = 0

    while len(lst1[i::]) > 0 and len(lst2[j::]) > 0:
        if lst1[i] < lst2[j]:
            combined.append(lst1[i])
            i += 1
        else:
            combined.append(lst2[j])
            j += 1
        
    if len(lst1[i::]) > 0:
        combined.extend(lst1[i::])
    else:
        combined.extend(lst2[j::])

    return combined

def merge_sort(unsorted):
    if len(unsorted) == 1:
        return unsorted
    
    mid = int(len(unsorted)/2)

    left = unsorted[:mid]
    right = unsorted[mid:]

    return merge(merge_sort(left), merge_sort(right))


x = [34,6,46,2,4,76,9,0,43,13,5,6,7,90,1,2134,56,8]

print(merge_sort(x))