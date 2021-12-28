from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        nodes = [root]
        left = True
        while nodes:
            children = []
            item = []
            count = len(nodes)
            for i in range(count):
                node = nodes[i] if left else nodes[count-i-1]
                item.append(node.val)

            for node in nodes:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            result.append(item)
            nodes = children
            left = False if left else True

        return result
