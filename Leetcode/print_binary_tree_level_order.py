from typing import List
from collections import deque
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
        nodes = deque([root])
        while nodes:
            node = nodes.popleft()
            result.append(node.val)
            nodes.append(node.left)
            nodes.append(node.right)
        return result
