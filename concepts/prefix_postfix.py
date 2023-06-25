# prefix sum
nums = [1,2,3,4,5]

prefix_sum = []
current_sum = 0
for num in nums:
    current_sum += num
    prefix_sum.append(current_sum)

print(prefix_sum)


# prefix product
nums = [1,2,3,4,5]

prefix_product = []
current_product = 1
for num in nums:
    current_product *= num
    prefix_product.append(current_product)

print(prefix_product)
