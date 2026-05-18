"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000 --> length of array is short and >=3
-105 <= nums[i] <= 105 ---> values can be large

for conditional application of the pointers, lets sort the array first.

lets say i iterated over the array.
build res=[[]]
for i in range():
        find sum=nums[j]+nums[k]+nums[i] with j starting at i+1 and k at nums.length-1
        > remember order of elements does not matter
        while j<=k:
                if sum<0:
                        j+=1
                        continue
                elif sum>0:
                        k-=1
                        continue
                else:
                        ele=[nums[i],nums[j],nums[k]]
                        res.append(ele)
"""

nums = [-1, 0, 1, 2, -1, -4]


def threeSum(nums):
    n = nums.__len__()
    nums.sort()
    res = []
    if n == 0:
        return res
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            print(sum)
            if sum < 0:
                j += 1
                continue
            elif sum > 0:
                k -= 1
                continue
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                # skip duplicates for j
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
    return res


print(threeSum(nums))
