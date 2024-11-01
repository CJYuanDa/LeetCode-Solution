from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        peri = 0

        # if the cell touch the boundary or the cell is next to the water
        # perimeter + 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # check top
                    if r == 0 or grid[r - 1][c] == 0:
                        peri += 1
                    # check bottom
                    if r == rows - 1 or grid[r + 1][c] == 0:
                        peri += 1
                    # check right
                    if c == cols - 1 or grid[r][c + 1] == 0:
                        peri += 1
                    # check left
                    if c == 0 or grid[r][c - 1] == 0:
                        peri += 1
        
        return peri