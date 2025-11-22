"""Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1."""


def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p3 = m + n - 1
    if nums2 != [] and nums1 == []:
        nums1[:] = nums2[:]
        return
    while p3 >= 0:
        if p1 < 0:
            nums1[p3] = nums2[p2]
            p3 -= 1
            p2 -= 1
            print("c")
        elif p2 < 0:
            break
        elif nums1[p1] > nums2[p2]:
            nums1[p3] = nums1[p1]
            p3 -= 1
            p1 -= 1
            print("a")
        elif nums1[p1] <= nums2[p2]:
            nums1[p3] = nums2[p2]
            p3 -= 1
            p2 -= 1
            print("b")
        print(nums1)


nums1 = []
m = 0
nums2 = [2, 5, 6]
n = 3
print(nums1)
merge(nums1, m, nums2, n)
print(nums1)
