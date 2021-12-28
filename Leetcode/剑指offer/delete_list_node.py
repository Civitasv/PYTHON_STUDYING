# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        fake = ListNode(0)
        fake.next = head
        temp = fake
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
        return fake.next
