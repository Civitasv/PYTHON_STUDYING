from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        i, j = 1, 2
        while i < j:
            j = ((1-4*(i-i**2-2*target))**0.5 - 1)/2
            if j == int(j) and i < j:
                res.append(list(range(i, int(j)+1)))
            i += 1
        return res
