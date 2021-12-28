# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        temp = head
        length = self.length(temp)
        res = [0 for _ in range(length)]
        for i in range(length):
            res[length-i-1] = temp.val
            temp = temp.next
        return res

    def length(self, head):
        if not head:
            return 0
        return 1 + self.length(head.next)


s = Solution()
l = ListNode(2)
l.next = ListNode(3)
res = s.reversePrint(l)
print(res)
