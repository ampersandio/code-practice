# prefix sum
nums = [1,2,3,4,5]

prefix_sum = []
current_sum = 0
for num in nums:
    current_sum += num
    prefix_sum.append(current_sum)

print(prefix_sum)


# prefix product

prefix_product = []
current_product = 1
for num in nums:
    current_product *= num
    prefix_product.append(current_product)

print(prefix_product)

# postfix sum 

postfix_sum = []
current_sum = 0
for num in nums[::-1]:
    current_sum += num
    postfix_sum.insert(0,current_sum)

print(postfix_sum)

# postfix product 

postfix_product = []
current_sum = 1
for num in nums[::-1]:
    current_sum *= num
    postfix_product.insert(0,current_sum)

print(postfix_product)
