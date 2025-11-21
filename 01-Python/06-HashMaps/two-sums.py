def two_sums(nums, target):
    seen = {}
    for i in range(len(nums)):
        c = target - nums[i]
        if c in seen.keys():
            return [i, seen[c]]
        else:
            seen[nums[i]] = i


nums = [2, 7, 11, 15]
target = 18
print(two_sums(nums, target))
