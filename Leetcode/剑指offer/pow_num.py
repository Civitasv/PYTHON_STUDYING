class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n == -1:
                return 1/x
            if n % 2 == 0:
                return pow(helper(n/2), 2)
            else:
                return pow(helper((n-1)/2), 2) * x

        return helper(n)


s = Solution()
print(s.myPow(2.00000, -2147483648))
