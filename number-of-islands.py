# Time Complexity = O(mn)
# Space Complexity = O(mn)
def numIslands(grid):
        if grid is None:
            return 0
        m = len(grid)
        n = len(grid[0])
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    islands += 1
        return islands
    
def dfs(grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != "1":
        return
    grid[i][j] = "visited"
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)