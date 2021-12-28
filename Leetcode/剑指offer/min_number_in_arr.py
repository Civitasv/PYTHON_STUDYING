from typing import List
from functools import cmp_to_key


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            astr = str(a)
            bstr = str(b)
            return 1 if (astr + bstr) > (bstr+astr) else -1
        nums.sort(key=cmp_to_key(compare))
        res = ""
        for num in nums:
            res += str(num)
        return res


s = Solution()
print(s.minNumber([824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247]))
