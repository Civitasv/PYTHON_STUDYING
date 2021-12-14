from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left, right, n = 0, 0, len(nums)

        # left 移动至第一个偶数
        while left < n:
            if nums[left] % 2 == 0:
                break
            left += 1
        right = left + 1
        while right < n:
            if nums[right] % 2 != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums


s = Solution()
l = [1, 2, 3, 4]
s.exchange(l)
print(l)
