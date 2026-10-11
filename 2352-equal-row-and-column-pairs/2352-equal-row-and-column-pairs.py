class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        cols = {}
        for i in range(n):
            key = tuple(grid[j][i] for j in range(n))
            cols[key] = cols.get(key, 0) + 1

        total = 0
        for row in grid:
            total += cols.get(tuple(row), 0)
        return total