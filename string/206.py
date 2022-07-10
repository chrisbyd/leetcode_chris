from typing import List
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        preNode = None
        newNode = None
        while head != None:
            newNode = ListNode(val= head.val)
            newNode.next = preNode
            preNode = newNode
            head = head.next
        return newNode




        