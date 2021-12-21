class Solution:
    def sumNums(self, n: int) -> int:
        if n == 0:
            return 0
        return n+self.sumNums(n-1)
