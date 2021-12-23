from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 相同的数异或为0，不同的数异或为1
        ret, index = 0, 0

        for num in nums:
            ret ^= num

        while ret & 1 == 0:
            index += 1
            ret >>= 1

        r1, r2 = 0, 0

        for num in nums:
            if (num >> index) & 1 == 0:
                r1 ^= num
            else:
                r2 ^= num

        return [r1, r2]
