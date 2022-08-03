# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        pred, cur = None, slow.next
        slow.next = None
        while cur:
            node = cur
            cur = cur.next
            node.next = pred
            pred = node
        cur1, cur2 = head, pred
        ans = 0
        while cur1:
            ans = max(ans, cur1.val + cur2.val)
            cur1 = cur1.next
            cur2 = cur2.next
        return ans
            
        
        