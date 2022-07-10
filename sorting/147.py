# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dp(head):
            if head.next is None:
                return ListNode(val = head.val)
            else:
                next_head = dp(head.next)
                cur = next_head
                prev = None
                while cur != None:
                    if head.val >= cur.val:
                        prev = cur
                        cur = cur.next
                    else:
                        break
                new_node = ListNode(val = head.val)
  
                if prev is not None:
                    head.next = prev.next
                    prev.next = head
                    return next_head
                else:
                    head.next = next_head
                    return head
        return dp(head)
                
                    


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        cur = ans = head
        while head:
            nums.append(head.val)
            head = head.next
            
        count = 0
        nums.sort()
        while cur:
            
            cur.val = nums[count]
            count+=1
            cur = cur.next
            
        return ans
        
        