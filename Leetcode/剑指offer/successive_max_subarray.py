from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]

        for i in range(0, n-1):
            dp[i+1] = max(dp[i]+nums[i+1], nums[i+1])
        res = dp[0]
        for i in range(0, n-1):
            res = max(res, dp[i+1])
        return res


s = Solution()
print(s.maxSubArray([3, 2, -3, -1, 1, -3, 1, -1]))
