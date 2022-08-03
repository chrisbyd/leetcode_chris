# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        value_list = []
        cur = head
        while cur:
            value_list.append(cur.val)
            cur = cur.next
        pos1, pos2 = k-1, len(value_list) - k
        tem = value_list[pos1]
        value_list[pos1] = value_list[pos2]
        value_list[pos2] = tem
        cur = head
        pointer = 0
        while cur:
            if cur.val != value_list[pointer]:
                cur.val = value_list[pointer]
            cur = cur.next
            pointer += 1
        return head


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        value_list = []
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        pos1, pos2 = k-1, length -k
        counter = 0
        cur = head
        while cur:
            if counter == pos1:
                left = cur
                break
            counter += 1
            cur = cur.next
        counter = 0 
        cur = head
        while cur:
            if counter == pos2:
                right = cur
                break
            counter += 1
            cur = cur.next
        tem = left.val
        left.val = right.val
        right.val = tem
        return head
        
       