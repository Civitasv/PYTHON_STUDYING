# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if (p.val <= root.val and root.val <= q.val) or (q.val <= root.val and root.val <= p.val):
                return root

            if p.val > root.val and q.val > root.val:
                return helper(root.right)

            if p.val < root.val and q.val < root.val:
                return helper(root.left)
        return helper(root)
