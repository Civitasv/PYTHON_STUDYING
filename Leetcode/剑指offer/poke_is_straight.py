from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        val = [0 for _ in range(14)]

        for num in nums:
            val[num] += 1

        for i in range(len(nums)-1):
            if nums[i] == 0:
                continue
            if nums[i+1] <= nums[i]:
                return False
            if nums[i+1]-nums[i] != 1:
                a = nums[i+1]-nums[i]-1
                if val[0] < a:
                    return False
                else:
                    val[0] -= a

        return True
