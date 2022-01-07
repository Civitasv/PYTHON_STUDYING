class Solution:
    """
    整数转罗马数字
    https://leetcode-cn.com/problems/integer-to-roman/
    """

    def intToRoman(self, num: int) -> str:
        dic = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        res = ""
        for k in dic.keys():
            while num >= k:
                res += dic[k]
                num -= k
        return res


s = Solution()
print(s.intToRoman(1994))
