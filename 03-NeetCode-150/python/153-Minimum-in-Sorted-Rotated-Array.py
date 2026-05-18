"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time

Input: nums = [3,4,5,1,2]
Output: 1

Input: nums = [4,5,6,7,0,1,2]
Output: 0

Input: nums = [11,13,15,17]
Output: 11

Solution approach:
Repeat:
        if nums[l]<=nums[r]:
                return nums[l]
        mid = l+(r-l)//2
        if nums[mid]<=nums[r]:
                r=mid
        else nums[mid]>nums[r]:
                l=mid+1
"""


def findMin(nums: list[int]):
    left = 0
    right = len(nums)-1
    while left <= right:
        if nums[left] <= nums[right]:
            return nums[left]
        mid = left + (right - left) // 2
        if nums[mid] <= nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]
    
print(findMin([4,5,6,7,10,55,1,2]))