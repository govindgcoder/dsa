"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

nums = [3,2,4]
target = 6

def twoSum(nums, target):
    hashmap = {}
    for i, ele in enumerate(nums):
        diff = target-ele
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[ele]=i

print(twoSum(nums,target))