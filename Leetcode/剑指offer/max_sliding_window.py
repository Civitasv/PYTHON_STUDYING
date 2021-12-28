from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        res = []
        q = deque()
        for i in range(n):
            while q and i - q[len(q)-1] >= k:
                q.pop()
            while q and nums[i] > nums[q[0]]:
                q.popleft()

            q.appendleft(i)
            if i >= k-1:
                res.append(nums[q[len(q)-1]])
        return res


s = Solution()
print(s.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
