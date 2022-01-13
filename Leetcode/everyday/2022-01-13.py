from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        maxNumIndex, secondMaxNumIndex = 0, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[maxNumIndex]:
                secondMaxNumIndex = maxNumIndex
                maxNumIndex = i
            elif nums[i] > nums[secondMaxNumIndex]:
                secondMaxNumIndex = i

        if nums[maxNumIndex] >= 2 * nums[secondMaxNumIndex]:
            return maxNumIndex
        else:
            return -1


s = Solution()
print(s.dominantIndex([1, 0]))
