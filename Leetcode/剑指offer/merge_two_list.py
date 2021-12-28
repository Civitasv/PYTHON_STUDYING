# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        fake = ListNode(0)

        temp = fake
        while l1 or l2:
            if not l1:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            elif not l2:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                if l1.val > l2.val:
                    temp.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    temp.next = ListNode(l1.val)
                    l1 = l1.next
            temp = temp.next
        return fake.next


s = Solution()

a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
d.next = e
e.next = f

s.mergeTwoLists(a, d)
