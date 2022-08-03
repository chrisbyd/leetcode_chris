# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
####dp will result in time exceed limit

#but it is coorect
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
        
#         """
#         Do not return anything, modify head in-place instead.
#         """
        
#         def dp(head):
#             if not head: return head
#             if not head.next: return head
#             if not head.next.next: return head
#             else:
#                 right = head
#                 pred = None
#                 while right and right.next:
#                     if right.next.next is None:
#                         pred = right
#                     right = right.next
#                 pred.next = None
#                 new_head = head.next
#                 head.next = right
#                 right.next = dp(new_head)
#                 printList(head)        
#                 return head
    
    
    
#         dp(head)
     
         
                
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
        node = ListNode(val = value)
        cur.next = node
        cur = cur.next
    return sentinel.next


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
        
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
        
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         v_list = []
#         cur = head
#         while cur:
#             v_list.append(cur.val)
#             cur = cur.next
#         length = len(v_list)
#         left, right = 0, length -1
#         ans = []
#         while left <= right:
#             if left == right:
#                 ans.append(v_list[left])
#             else:
#                 ans.append(v_list[left])
#                 ans.append(v_list[right])
#             left += 1
#             right -= 1
     
#         cur = head
#         for val in ans:
#             cur.val = val
#             cur = cur.next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:  
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        first_half = head
        second_half = slow.next
        slow.next = None
        
        ##reverse second half
        pred, cur = None, second_half
   
        while cur:
            node = cur
            cur = cur.next
            node.next = pred
            pred = node

        second_half = pred
        cur1, cur2 = first_half, second_half

        pred = ListNode()
        while cur1:
            node1 = cur1
            node2 = cur2
            cur1 = cur1.next
            cur2 = cur2.next if  cur2 else None
            pred.next = node1
            node1.next = node2
            pred = node2


sol = Solution()
head = constructList([1,2,3,4])
res = sol.reorderList(head)
