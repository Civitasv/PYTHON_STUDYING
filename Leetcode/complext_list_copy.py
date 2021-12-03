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

        temp = head
        while temp:
            node = Node(temp.val, temp.next)
            temp.next = node
            temp = temp.next.next

        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        temp = head.next
        while temp.next:
            temp.next = temp.next.next
            temp = temp.next

        return head.next


a = Node(7)
b = Node(13)
c = Node(11)
d = Node(10)
e = Node(1)

a.next = b
b.next = c
c.next = d
d.next = e

b.random = a
c.random = e
d.random = c
e.random = a

s = Solution()

ac = s.copyRandomList(a)

while ac:
    print(ac.val)
    ac = ac.next
