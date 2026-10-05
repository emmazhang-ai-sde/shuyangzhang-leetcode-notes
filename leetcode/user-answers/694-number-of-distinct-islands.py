# 694. Number of Distinct Islands
# Shuyang 自写答案，2026-08-19。
# 思路：对每座岛 DFS，把每个格子相对起点 (startRow, startCol) 的偏移记下来，
# 形状相同的岛偏移序列一样，最后数 set 里有几种。

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        shapes = set()


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    island = []
                    self.dfs(grid, visited, row, col, row, col, island)
                    shapes.add(tuple(island))
        return len(shapes)

    def dfs(self,grid, visited, startRow, startCol,currRow, currCol, island):

        visited.add((currRow, currCol))
        island.append((currRow - startRow, currCol - startCol))

        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            newRow = currRow + dx
            newCol = currCol + dy

            if not (0<=newRow<len(grid) and 0<=newCol<len(grid[0])):
                continue

            if grid[newRow][newCol] != 1:
                continue
            if (newRow, newCol) in visited:
                continue

            self.dfs(grid, visited, startRow, startCol,newRow, newCol, island)
