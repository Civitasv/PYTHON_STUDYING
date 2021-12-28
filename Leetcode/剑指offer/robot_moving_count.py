class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def val(a):
            sum = 0
            while a != 0:
                sum += a % 10
                a //= 10
            return sum

        def helper(i, j, vi):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if vi[i][j]:
                return 0
            if val(i) + val(j) > k:
                return 0

            vi[i][j] = True
            ans = 1+helper(i+1, j, vi)+helper(i-1, j, vi) + \
                helper(i, j-1, vi)+helper(i, j+1, vi)
            return ans
        vi = [[False]*n for _ in range(m)]
        return helper(0, 0, vi)


s = Solution()
print(s.movingCount(3, 1, 0))
