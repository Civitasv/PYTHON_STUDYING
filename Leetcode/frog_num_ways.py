class Solution:
    def numWays(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        mod = 1e9+7
        for i in range(2, n):
            dp[i] = int((dp[i-2] % mod + dp[i-1] % mod) % mod)

        return dp[n-1]


s = Solution()
print(s.numWays(7))
