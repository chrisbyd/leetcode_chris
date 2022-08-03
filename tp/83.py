# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(val = 0, next = head)
        first = head
        pred = head
        while head:
            if head.next and head.val == head.next.val:
                head = head.next
            else:
               
                pred.next = head.next
                pred = head.next
                head = head.next
        return first
                
            
        