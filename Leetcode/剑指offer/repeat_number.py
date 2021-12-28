from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        arr = [-1 for _ in range(len(nums))]
        for num in nums:
            if arr[num] != -1:
                return num
            arr[num] = num

    def helper(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            num = nums[i]
            a = nums[num]
            if a == num:
                return a
            nums[num] = num
            nums[i] = a
