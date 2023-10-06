class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        per=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    per+=4
                    if i>0 and grid[i-1][j]==1:
                        per-=2
                    if j>0 and grid[i][j-1]==1:
                        per-=2
        return per
