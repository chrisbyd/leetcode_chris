# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

                
def printList(node):
    cur = node
    ans = []
    while cur:
        ans.append(cur.val)
        cur = cur.next     
    print(ans)

def constructList(v_list):
    sentinel = ListNode()
    cur = sentinel
    for value in v_list:
        node = ListNode(x = value)
        cur.next = node
        cur = cur.next
    return sentinel.next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast  = head, head
        
        #detect cycle
        cycle = 0
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                cycle = 1
                break
        
        if cycle == 0:
            return None
       # printList(slow)
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        slow.next = None
        return slow
        # printList(slow)


sol = Solution()
head = constructList([1,2,3,4])
cur  = head
while cur.next:
    cur = cur.next
cur.next = head
res = sol.detectCycle(head)
printList(res)


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare = head
        tortoise = head
        res = None
        
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            
            
            if hare == tortoise:
                res = hare
                break
        
        if not res:
            return res
        
        hare = head
        
        while hare != tortoise:
            hare = hare.next
            tortoise = tortoise.next
        
        return  ListNode(tortoise.val)    


sol = Solution()
head = constructList([1,2,3,4])
cur  = head
while cur.next:
    cur = cur.next
cur.next = head
res = sol.detectCycle(head)
printList(res)
