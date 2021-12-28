from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1

        for x in h:
            if h[x] > len(nums)//2:
                return x

    def moer(self, nums):
        res, count = 0, 0

        for num in nums:
            if count == 0:
                res = num
                count = 1
            else:
                if res == num:
                    count += 1
                else:
                    count -= 1
        return res


s = Solution()
print(s.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
