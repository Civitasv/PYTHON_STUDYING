from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分法
        def helper(target):
            low, hi = 0, len(nums)-1
            while low <= hi:
                mid = (low+hi)//2
                # low 表示所有大于等于target值的开始索引
                if nums[mid] < target:
                    low = mid+1
                # hi 表示所有小于target值的开始索引
                else:
                    hi = mid-1
            return low
        return helper(target+1) - helper(target)


s = Solution()
print(s.search([5, 7, 7, 8, 8, 10], 8))
