class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i,j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
                grid[i][j] = 0
                map(sink, (i+1, i-1, i),(j,j,j+1,j-1))
                return 1
            return 0
        return sum(sink(i,j) for i in range(len(grid)) for j in range(len(grid[i])))


if __name__ == '__main__':
    grid=[[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0,],[0,0,0,1,1]]
    print(Solution().numIslands(grid))
