A = [0, 1, 2, 3, 4] 

def build_prefix_sum(nums):
    result = list(0 for i in range(len(nums)+1))
    for i, val in enumerate(nums):
        result[i+1]=result[i]+val
    return result

print(A)
B = build_prefix_sum(A)
print(B)
# Expected output: [0, 1, 3, 6, 10]