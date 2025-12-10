"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where
1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Constant extra space

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Solution:

- numbers are in ascending order.
- lets think of 2 pointers

fp starts at 0, lp starts at n-1
if nums[fp]+nums[lp]=sum:
    return [fp+1,lp+1]
if nums[fp]+nums[lp]<sum:
    fp+=1
if nums[fp]+nums[lp]>sum:
    lp-=1

"""


def twoSum(numbers, target):
    fp, lp = 0, len(numbers) - 1
    while fp <= lp:
        sum = numbers[fp] + numbers[lp]
        if sum == target:
            return [fp + 1, lp + 1]
        elif sum < target:
            fp += 1
        else:
            lp -= 1


print(twoSum([2, 3, 4], 6))
