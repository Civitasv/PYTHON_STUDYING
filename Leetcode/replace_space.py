class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ""
        for c in s:
            print(c)
            if c == ' ':
                res += "%20"
            else:
                res += c
        return res


s = Solution()
print(s.replaceSpace("We are champion"))
