# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(root):
            if not root:
                return

            helper(root.left)
            if not self.pre:  # 最小值没有前驱节点
                self.head = root
            else:
                self.pre.right = root  # 前驱的后继是当前
                root.left = self.pre  # 后继的前驱是前驱
            self.pre = root  # 保存前驱

            helper(root.right)

        if not root:
            return

        self.pre, self.head = None, None
        helper(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
