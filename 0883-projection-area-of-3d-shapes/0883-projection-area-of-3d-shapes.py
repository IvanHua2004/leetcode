class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        total = 0
        for bloc in grid:
            maximum = 0
            for tile in bloc:
                if tile > 0:
                    total += 1
                if tile > maximum:
                    maximum = tile
            total += maximum

        for j in range(len(grid[0])):
            maximum = 0
            for i in range(len(grid)):
                if grid[i][j] > maximum:
                    maximum = grid[i][j]
            total += maximum
        
        return total
