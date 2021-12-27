class Solution:
    def strToInt(self, str: str) -> int:

        def whiteSpace(i):
            while i < len(str) and str[i] == ' ':
                i += 1

            return i

        def integer(i):
            res = ""
            if i < len(str) and (str[i] == '+' or str[i] == '-'):
                res += str[i]
                i += 1
            while i < len(str) and str[i].isdigit():
                res += str[i]
                i += 1
            return res

        a = 2**31-1
        b = -2**31
        i = 0
        i = whiteSpace(i)
        res = integer(i)

        if res == "" or res == '+' or res == '-':
            return 0
        else:
            c = int(res)
            if c > a:
                return a
            elif c < b:
                return b

            return int(res)


s = Solution()
print(s.strToInt("-91283472332"))
