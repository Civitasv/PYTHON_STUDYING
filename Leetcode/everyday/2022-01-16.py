from typing import Optional
import random
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        p = self.head
        count, res = 0, 0
        while p:
            count += 1
            rand = random.randint(count)+1
            if rand == count:
                res = p.val
            p = p.next

        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
