# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sentinel = ListNode()
        cur = sentinel
        while l1 and l2:
            cval = l1.val + l2.val + carry
            carry = cval // 10
            cval = cval % 10
            nnode = ListNode(val = cval)
            cur.next =nnode
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
            
        while l1: 
            cval = l1.val + carry
            carry = cval // 10
            cval = cval % 10
            nnode = ListNode(val = cval)
            cur.next = nnode
            cur = cur.next
            l1 = l1.next
            
        while l2: 
            cval = l2.val + carry
            carry = cval // 10
            cval = cval % 10
            nnode = ListNode(val = cval)
            cur.next = nnode
            cur = cur.next
            l2 = l2.next
        if carry:
            cur.next = ListNode(val = 1)
        return sentinel.next