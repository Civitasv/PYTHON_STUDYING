class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        n = len(s)
        a = b = 1

        for i in range(2, n+1):
            b, a = a+b if "10" <= s[i-2:i] <= "25" else b, b
        return b
