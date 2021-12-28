class Solution:
    def add(self, a: int, b: int) -> int:
        c = 0xffffffff
        a, b = a & c, b & c
        while True:
            x = a ^ b
            y = ((a & b) << 1) & c
            if y == 0:
                return x if x <= 0x7fffffff else ~(x ^ c)
            a = x
            b = y
