from typing import List


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []

        def helper(path, sum, root):
            if sum == target:
                if root and not root.right and not root.left:
                    res.append(path.copy())
                    return

            if not root:
                return

            if root.left:
                sum += root.left.val
                path.append(root.left.val)
                helper(path, sum, root.left)
                sum -= root.left.val
                path.pop()

            if root.right:
                sum += root.right.val
                path.append(root.right.val)
                helper(path, sum, root.right)
                sum -= root.right.val
                path.pop()
        if not root:
            return res
        helper([root.val], root.val, root)
        return res


root = TreeNode(-2)
root.right = TreeNode(-3)
s = Solution()
print(s.pathSum(root, -5))
