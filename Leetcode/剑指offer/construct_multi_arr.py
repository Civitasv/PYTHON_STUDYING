from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        res = [0 for _ in range(len(a))]

        # 先乘以左边的数
        cur = 1
        for i in range(len(a)):
            res[i] = cur
            cur *= a[i]

        # 再乘以右边的数
        cur = 1
        for i in range(len(a)-1, -1, -1):
            res[i] *= cur
            cur *= a[i]
        return res
