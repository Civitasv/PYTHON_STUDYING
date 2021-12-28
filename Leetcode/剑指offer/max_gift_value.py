from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        def value(i, j):
            if i >= 0 and i < m and j >= 0 and j < n:
                return dp[i][j]
            return 0

        for i in range(m):
            for j in range(n):
                dp[i][j] = max(value(i, j-1), value(i-1, j)) + grid[i][j]
        return dp[m-1][n-1]


s = Solution()
print(s.maxValue([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
