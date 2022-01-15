class Solution:
    def totalMoney(self, n: int) -> int:
        start, cycle = -1, 7
        total = 0
        for i in range(1, n+1):
            if i % cycle == 1:
                start += 1
            if i % cycle == 0:
                total += start+cycle
            else:
                total += (start+i % cycle)
        return total


s = Solution()
print(s.totalMoney(10))
