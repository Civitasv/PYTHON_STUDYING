# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        fake = Node(0)
        tfake = fake
        hset = {}
        temp = head
        while temp:
            node = Node(temp.val)
            tfake.next = node
            hset[]
            random = temp.random
            rnode = Node(random.val, random.next)
            if rnode in set:
                node.random = rnode
