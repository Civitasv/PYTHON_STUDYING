# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> TreeNode:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        nodes = [root.left, root.right]
        while nodes:
            children = []
            for i in range(len(nodes)//2):
                a = nodes[i]
                b = nodes[len(nodes)-i-1]
                if a.val != b.val:
                    return False

                if (a.left != None) != (b.right != None):
                    return False
                if (a.right != None) != (b.left != None):
                    return False
                if a.left and b.right:
                    if a.left.val != b.right.val:
                        return False
                if a.right and b.left:
                    if a.right.val != b.left.val:
                        return False

            for node in nodes:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)

            nodes = children
        return True

    def isSymmetric2(self, root):
        def helper(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            return helper(l.left, r.right) and helper(l.right, r.left)
        return helper(root.left, root.right) if root else True
