from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for push in pushed:
            stack.append(push)
            while i < len(popped) and stack and stack[len(stack)-1] == popped[i]:
                stack.pop()
                i += 1
        return i == len(popped)


s = Solution()

print(s.validateStackSequences([2, 1, 0], [1, 2, 0]))
