class Solution:
    def isNumber(self, s: str) -> bool:
        def whiteSpace(i):
            while i < len(s) and s[i] == ' ':
                i += 1

            return i

        def integer(i):
            res = False
            if i < len(s) and (s[i] == '+' or s[i] == '-'):
                i += 1
            while i < len(s) and s[i].isdigit():
                res = True
                i += 1
            return res, i

        def decimal(i):
            res = False
            if i < len(s) and (s[i] == '+' or s[i] == '-'):
                i += 1
            if i < len(s) and s[i] == '.':
                i += 1
                while i < len(s) and s[i].isdigit():
                    res = True
                    i += 1
            else:
                while i < len(s) and s[i].isdigit():
                    res = True
                    i += 1
                if i < len(s) and s[i] == '.':
                    i += 1
                    while i < len(s) and s[i].isdigit():
                        res = True
                        i += 1
            return res, i

        def e(i):
            res = True
            if i < len(s):
                if (s[i] == 'e' or s[i] == 'E'):
                    res, i = integer(i+1)

            return res, i

        a = whiteSpace(0)
        res, a = decimal(a)
        if not res:
            return False
        res, a = e(a)
        if not res:
            return False
        a = whiteSpace(a)

        return a == len(s)


s = Solution()
print(s.isNumber("0"))
