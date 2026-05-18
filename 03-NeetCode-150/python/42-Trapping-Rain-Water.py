"""
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
Example:
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9

Solution:

Water can only be trapped between two bars - bars between two bars needs to be smaller than the minimum of the two heights. - minimum height of the two bars x the width gives the area.

Build arrays storing the max left and max left above each element.

"""

height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]

# O(n) space
# def trapRain(height):
#     # also for right
#     print(height)
    # if not height:
    #     return 0
    # n = len(height)
    # maxl = height[0]
    # maxr = height[-1]
    # res = []
    # for i in range(n):
    #     maxl=max(maxl, height[i])
    #     res.append(maxl)
    # print(res)
    # for i in range(n - 1, -1, -1):
    #     maxr=max(maxr, height[i])
    #     res[i] = min(maxr, res[i]) - height[i]
    # sum = 0
    # for i in res:
    #     sum += i
    # return sum

#O(1) space two pointer solution
def trapRain(height):
    if not height:
        return 0
    lp = 0
    rp = len(height) - 1
    maxl = height[0]
    maxr = height[-1]
    area = 0
    while lp < rp:
      maxl = max(maxl, height[lp])
      maxr = max(maxr, height[rp])
      if maxl < maxr:
         area += maxl - height[lp]
         lp += 1
      else:
         area += maxr - height[rp]
         rp -= 1
    return area


print(trapRain(height))
