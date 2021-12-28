# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        def helper(root):
            if not root:
                return True
            return abs(depth(root.left) - depth(root.right)) <= 1 and helper(root.left) and helper(root.right)
        return helper(root)
