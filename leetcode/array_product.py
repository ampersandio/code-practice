"238. Product of Array Except Self"

nums = [1,2,3,4]


def productExceptSelf(self, nums):

    prefix = [1] * len(nums)

    for i in range(len(nums)):
        prefix[i] = nums[i] * prefix[i-1]

    postfix = [1] * len(nums)

    for i in range(len(nums)):
        postfix[i] = nums[::-1][i] * postfix[i-1]

    postfix = postfix[::-1]

    new_lst = []

    for i in range(len(nums)):

        if i-1 == -1:
            pre = 1
        else:
            pre = prefix[i-1]
        if i + 1 == len(nums):
            post = 1    
        else:
            post = postfix[i+1]
        new_lst.append(pre * post)

    return(new_lst)