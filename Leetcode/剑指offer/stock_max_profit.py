from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp = [0 for _ in range(n)]
        min_price = prices[0]

        for i in range(1, n):
            dp[i] = max(dp[i-1], prices[i]-min_price)
            min_price = min(min_price, prices[i])
        return dp[n-1]
