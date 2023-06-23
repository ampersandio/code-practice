# lst = [1,2,3] 
# target = 4

# hash_map = {}

# for index,item in enumerate(lst):
#     diff = target - item

#     if diff in hash_map:
#         print(hash_map[diff], index)
#     else:
#         hash_map[item] = index


lst = [1,2,3] 
target = 4


def two_sum(lst, target):
    hash_map = {}

    for index,item in enumerate(lst):
        difference = target - item

        if difference in hash_map:
            return (hash_map[difference], index)

        else:
            hash_map[item] = index


print(two_sum(lst,target))