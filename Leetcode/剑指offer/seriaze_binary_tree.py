from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        queue = [root]
        res = []
        flag = True
        while flag:
            next = []
            flag = False
            for i in range(len(queue)):
                node = queue[i]
                if node:
                    res.append(str(node.val))

                    if node.left or node.right:
                        flag = True
                    next.append(node.left)
                    next.append(node.right)
                else:
                    res.append("null")
            queue = next
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(nodes[0])
        queue = deque([root])
        i = 1
        while queue and i < len(nodes):
            node = queue.popleft()
            if i < len(nodes):
                left = nodes[i]
            else:
                left = 'null'
            i += 1
            if i < len(nodes):
                right = nodes[i]
            else:
                right = 'null'
            i += 1
            if left != 'null':
                leftN = TreeNode(int(left))
                node.left = leftN
                queue.append(leftN)
            if right != 'null':
                rightN = TreeNode(int(right))
                node.right = rightN
                queue.append(rightN)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
s = Codec()
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(1)
d = TreeNode(3)
g = TreeNode(2)
h = TreeNode(4)

root.left = b
b.right = h
# root.right = b
# a.left = c
# a.right = d
# b.left = g
# b.right = h

e = s.serialize(root)
print(e)
f = s.deserialize(e)
print(f)
