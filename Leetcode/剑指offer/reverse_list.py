class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead


s = Solution()
l = ListNode(2)
b = ListNode(3)
l.next = b
b.next = ListNode(4)
rl = s.reverseList(l)
while rl:
    print(rl.val)
    rl = rl.next
