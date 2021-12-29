from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        def helper(item, s):
            if len(item) == len(s):
                res.append(item)
                return
            cache = []
            for i in range(len(s)):
                if vi[i]:
                    continue
                if s[i] in cache:
                    continue
                cache.append(s[i])
                vi[i] = True
                helper(item+s[i], s)
                vi[i] = False
        vi = [False for _ in range(len(s))]
        res = []
        helper("", s)
        return res


s = Solution()
print(s.permutation("aab"))
