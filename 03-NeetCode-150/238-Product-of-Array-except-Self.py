"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

1,2,3,4
p:1,1,1x2,3x2x1
s:2x3x4,3x4,4,1
res=s[i]*p[i]
"""
nums = [1,2,3,4]

def pdts(nums):
    n = len(nums)
    res=[1]*n
    x=1
    #calculate prefix products
    for i in range(1,n):
            res[i]=nums[i-1]*res[i-1]
    #calculate postfix products and update it to result on the fly
    # current postfix product is x
    for i in range(n-2,-1,-1):
            x=nums[i+1]*x
            res[i]=res[i]*x
    return res
print(pdts(nums))