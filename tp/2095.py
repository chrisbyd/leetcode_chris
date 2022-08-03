from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return head
            
        
        