"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

nums = [1,2,3,4]

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hashset = set()
    for curr in nums:
        if curr in hashset:
            return True
        hashset.add(curr)
    return False

print(containsDuplicate(nums))
    