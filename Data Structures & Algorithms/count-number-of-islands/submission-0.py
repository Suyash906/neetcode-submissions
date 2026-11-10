class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(row, col):
            ## base
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != '1':
                return

            ## body
            grid[row][col] = '0'

            for x, y in dirs:
                nx, ny = x + row, y + col
                dfs(nx, ny)

        res = 0
        
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == '1':
                    res += 1
                    dfs(i, j)

        return res