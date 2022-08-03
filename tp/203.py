from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode()
        pred, cur = sentinel,  head
        while cur:
            if cur.val == val:
                pred.next = cur.next
            else:
                pred.next = cur
                pred = cur
            cur = cur.next
        return sentinel.next
        
        