class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        d = {}
        total = 0

        for i in range(n):
            key = tuple([grid[j][i] for j in range(n)])
            d[key] = d.get(key, 0) + 1
        
        for row in grid:
            total += d.get(tuple(row), 0)
        
        return total