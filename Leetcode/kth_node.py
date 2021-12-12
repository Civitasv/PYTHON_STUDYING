# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head

        while fast and k > 0:
            fast = fast.next
            k -= 1

        while fast:
            slow = slow.next
            fast = fast.next
        return slow
