# You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
         
        m, n = len(grid), len(grid[0])

        for layer in range(min(m, n) // 2):
            top = [grid[layer][j] for j in range(layer, n - 1 - layer)]
            right = [grid[i][n - 1 - layer] for i in range(layer, m - 1 - layer)]
            bottom = [grid[m - 1 - layer][j] for j in range(n - 1 - layer, layer, -1)]
            left = [grid[i][layer] for i in range(m - 1 - layer, layer, -1)]
            
            flat = top + right + bottom + left

            shift = k % len(flat)
            rotated = flat[shift:] + flat[:shift]

            idx = 0

            for j in range(layer, n - 1 - layer): grid[layer][j] = rotated[idx]; idx += 1
            for i in range(layer, m - 1 - layer): grid[i][n - 1 - layer] = rotated[idx]; idx += 1
            for j in range(n - 1 - layer, layer, -1): grid[m - 1 - layer][j] = rotated[idx]; idx += 1
            for i in range(m - 1 - layer, layer, -1): grid[i][layer] = rotated[idx]; idx += 1
        return grid
