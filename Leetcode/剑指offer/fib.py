class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        a, b, mod = 0, 1, 1e9+7
        for _ in range(2, n+1):
            c = (a % mod + b % mod) % mod
            a = b
            b = c
        return int(b)


s = Solution()
print(s.fib(5))
