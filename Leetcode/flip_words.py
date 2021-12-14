class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        i = len(s)-1
        while i >= 0:
            while i >= 0 and s[i] == " ":
                i -= 1
            j = i
            while i >= 0 and s[i] != " ":
                i -= 1
            if j > i:
                res += s[i+1:j+1]
                res += " "
        return res[0:len(res)-1]
