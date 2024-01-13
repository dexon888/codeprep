def numIslands(self, grid):
    result = 0
    visited = set()

    def dfs(i, j):
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == "0" or (i, j) in visited:
            return
        visited.add((i, j))
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and (i, j) not in visited:
                result += 1
                dfs(i, j)
    return result
