from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(inorder, start, end, val):
            for i in range(start, end+1):
                if inorder[i] == val:
                    return i

        def dfs(preorder, inorder, prestart, preend, instart, inend):
            if prestart > preend:
                return
            root = TreeNode(preorder[prestart])
            partition = helper(inorder, instart, inend, preorder[prestart])
            root.left = dfs(preorder, inorder, prestart+1,
                            prestart+partition-instart, instart, partition-1)
            root.right = dfs(preorder, inorder, prestart +
                             partition-instart+1, preend, partition+1, inend)
            return root

        if not preorder:
            return None
        return dfs(preorder, inorder, 0, len(preorder)-1, 0, len(preorder)-1)
