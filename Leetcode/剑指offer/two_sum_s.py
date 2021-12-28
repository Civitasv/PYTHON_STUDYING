from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right, n = 0, 1, len(nums)
        forward = True
        if n < 2:
            return [-1, -1]
        while left != right:
            a = nums[left] + nums[right]
            if a < target:
                if forward and right < n-1:
                    right += 1
                else:
                    left += 1
                    forward = True
            elif a > target:
                if right - left > 1:
                    right -= 1
                    forward = False
                else:
                    return [-1, -1]
            else:
                return [nums[left], nums[right]]
        return [-1, -1]

    def twoSum2(self, nums, target):
        left, right = 0, len(nums)-1

        while left < right:
            a = nums[left] + nums[right]

            if a > target:
                right -= 1
            elif a < target:
                left += 1
            else:
                return [nums[left], nums[right]]


s = Solution()
print(s.twoSum([45, 46, 67, 73, 74, 74, 77, 83, 89, 98], 147))
