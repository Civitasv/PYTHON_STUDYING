class Solution:
    """
    括号的最大嵌套深度
    https://leetcode-cn.com/problems/maximum-nesting-depth-of-the-parentheses/
    """

    def maxDepth(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                right += 1
            res = max(res, left-right)
        return res


s = Solution()
print(s.maxDepth("(1+(2*3)+((8)/4))+1"))
