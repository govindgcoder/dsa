grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","1"],
  ["0","0","0","1","0"]
]

def countIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def search(r,c):
        if r>=rows or r<0 or c<0 or c>=cols or grid[r][c]=="0":
            return False
        grid[r][c]="0"
        search(r-1,c)
        search(r+1,c)
        search(r,c-1)
        search(r,c+1)
        return True
    
    for i in range(rows):
        for j in range(cols):
            if search(i,j):
                count+=1
    
    return count
    
print(countIslands(grid))