nums = [1, 2, 3]


def subsets(nums):
    result = []
    n = len(nums)

    def backtrack(index, curr):
        result.append(curr[:])
        for i in range(index, n):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

    backtrack(0, [])
    return result


print(subsets(nums))
