class Solution:
    area = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid = self.recurse(grid,i,j)
                    maxarea = max(Solution.area,maxarea)
                    Solution.area = 0
        return maxarea

    def recurse(self,grid: List[List[int]],i: int,j: int):
        if i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
            return grid
        grid[i][j] = 0
        Solution.area += 1
        grid = self.recurse(grid,i,j+1)
        grid = self.recurse(grid,i+1,j)
        if i > 0:
            grid = self.recurse(grid,i-1,j)
        if j > 0:
            grid = self.recurse(grid,i,j-1)
        return grid