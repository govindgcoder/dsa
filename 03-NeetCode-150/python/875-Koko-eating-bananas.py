"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Here h is always greater than or equal to the length of the array.

- slowest speed koko can eat is 1 bananas/hour
- fastest = maximum no of bananas of pile array

for a pile with x bananas, time for eating = (x+k-1)//k to get the effect of division and one more hours for the values less than k
if total hours <= h try with a lower value for k
if total hours > h try with a faster value for k

return 0 if the array is empty
start with k having the maximum value of the number of bananas.
using a while loop such that calculated total hours <= h: decrement k after each session
output the final value.

but this is a linear search

to improve speed, we can initialize a k array with values from k=1 to k=max(piles)
using binary search on this array to take mid and do the calculation for total hours H and check it while it is less than h. if H is > h, then check the right half, otherwise continue checking the left half until left<=right while loop ends.

a virtual array can be used to get this effect by taking right as mid-1 and left as mid+1 when needed.
"""


def minEatingSpeed(piles: list[int], h: int):
    left = 1
    right = max(piles)
    res = right
    while left <= right:
        mid = left + (right - left) // 2
        total = 0
        for pile in piles:
            total += (pile + mid - 1) // mid
        print(total, " ", mid)
        if total <= h:
            right = mid -1
            res = mid
        else:
            left = mid + 1
    return res


print(minEatingSpeed(piles = [30,11,23,4,20], h = 6))
