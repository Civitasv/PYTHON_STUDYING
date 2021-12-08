# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def helper(A, B):
            if not B:
                return True
            if not A:
                return False
            if A.val != B.val:
                return False

            return helper(A.left, B.left) and helper(A.right, B.right)
        if not B:
            return False
        if not A:
            return False
        return helper(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
