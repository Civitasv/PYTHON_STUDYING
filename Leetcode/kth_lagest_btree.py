# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def helper(root):
            if not root:
                return
            if self.index == k:
                return

            helper(root.right)

            self.index += 1
            if self.index == k:
                self.res = root.val

            helper(root.left)
        self.res = 0
        self.index = 0
        helper(root)
        return self.res


root = TreeNode(3)
a = TreeNode(1)
b = TreeNode(4)
c = TreeNode(2)

root.left = a
root.right = b
a.right = c

s = Solution()
print(s.kthLargest(root, 2))
