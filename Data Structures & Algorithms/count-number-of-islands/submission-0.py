class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    n += 1
                    grid = recurse(grid,i,j)
        return n

def recurse(grid,i,j):
    if i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
        return grid
    grid[i][j] = "0"
    grid = recurse(grid,i,j+1)
    grid = recurse(grid,i+1,j)
    if i > 0:
        grid = recurse(grid,i-1,j)
    if j > 0:
        grid = recurse(grid,i,j-1)
    return grid