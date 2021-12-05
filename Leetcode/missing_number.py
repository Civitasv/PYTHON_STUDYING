from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        low = 0
        hi = len(nums) - 1

        while low <= hi:
            mid = (low + hi) // 2
            if nums[mid] == mid:
                low = mid + 1
            else:
                hi = mid - 1
        return low
