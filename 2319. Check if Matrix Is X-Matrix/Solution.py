class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        rows=len(grid)
        for i in range(rows):
            if grid[i][i]==0:
                return False
            if grid[i][rows-i-1]==0:
                return False
            for j in range(rows):
                if i!=j and i!=rows-j-1:
                    if grid[i][j]!=0:
                        return False
        return True
