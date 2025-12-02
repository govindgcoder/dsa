"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
"""

def uniquePaths(m,n):
    ways = [[1]*n for _ in range(m)]
    for r in range(1,m):
        for c in range(1,n):
            x=r-1
            y=c-1
            ways[r][c]=ways[x][c]+ways[r][y]
    return ways[m-1][n-1]
m = 3
n = 2
print(uniquePaths(m,n))

# ways for each cell is the stuff