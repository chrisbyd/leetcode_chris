# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value_list = []
        if not head: return head
        cur = head
        while cur:
            value_list.append(cur.val)
            cur = cur.next
        counter = 1
        length = len(value_list)
        value_list = [101] + value_list + [101]
        new_val_list = []
        for i in range(1, length + 1):
            if  value_list[i] != value_list[i-1] and value_list[i] != value_list[i+1]:
                new_val_list.append(value_list[i])
        if not new_val_list: return None
        new_root = ListNode()
        cur = new_root 
        index = 0
        while index < len(new_val_list):
            cur.val = new_val_list[index]
            if index != len(new_val_list) -1:
                cur.next = ListNode()
                cur = cur.next
            index += 1
        return new_root
            
### with two pointer solution
# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head
        sentinel = ListNode(val = 102)
        sentinel.next = head
        prev = sentinel.val
        left, right = sentinel, head
        while right:
            if right.val != prev and (not right.next or right.next.val != right.val):
                left.next = right
                left = right
            prev = right.val
            right = right.next
        left.next = right
        return sentinel.next
                
                
        

# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        ### predecessor = the last node
        pred = sentinel
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next 
        return sentinel.next
            
                
        
        
        
                
                
        
        
        
        

