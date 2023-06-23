x = [5, 2, 3, 5, 2, 2, 3, 5, 1, 2, 5, 1, 2, 5, 3]
step = 7


def array_normalization(lst, step):
    nums = set(lst)

    counts = []

    for i in nums:

        index = 0
        count = 0

        while index < len(x):

            if lst[index] != i:
                count += 1
                index += step
            else:
                index += 1

        counts.append(count)

    return(min(counts))


print(array_normalization(x,step))