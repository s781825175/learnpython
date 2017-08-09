class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum((grid[i][j]==1)*4-(grid[i][j]==grid[i][j-1]==1 and j!=0)*2-(grid[i][j]==grid[i-1][j]==1 and i!=0)*2 for i in range(len(grid))for j in range(len(grid[0])))
a=Solution()
grid=[[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
l=a.islandPerimeter(grid)
print(l)
