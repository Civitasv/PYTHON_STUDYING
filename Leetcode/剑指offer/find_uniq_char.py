class Solution:
    def firstUniqChar(self, s: str) -> str:
        alphabets = [0 for _ in range(26)]
        for c in s:
            alphabets[ord(c)-97] += 1

        for c in s:
            if alphabets[ord(c)-97] == 1:
                return c
        return " "


s = Solution()
print(s.firstUniqChar("aadadaad"))
