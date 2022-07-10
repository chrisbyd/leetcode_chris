from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        ans = cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        nums.sort()
        count = 0
        while ans:
            ans.val = nums[count]
            ans = ans.next
            count += 1
        return head
        
        