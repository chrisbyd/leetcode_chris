# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return head
        v_list = []
        cur = head
        while cur:
            v_list.append(cur.val)
            cur = cur.next
        n_v_list, r_v_list = [], []
        for num in v_list:
            if num < x:
                n_v_list.append(num)
            else:
                r_v_list.append(num)
        n_v_list = n_v_list + r_v_list
        new_head = ListNode()
        cur = new_head
        for i in range(len(v_list)):
            cur.val = n_v_list[i]
            if i != len(v_list) -1:
                node = ListNode()
                cur.next = node
                cur = cur.next
        return new_head

###another solution

# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sentinel = ListNode(val = 0, next= head)
        l_head = ListNode(val = 0)
        cur = head
        pred_l = sentinel
        pred_r = l_head
        while cur:
            if cur.val < x:
                pred_l.next = cur
                pred_l = pred_l.next
            else:
                pred_r.next = cur
                pred_r = pred_r.next
            old_cur = cur
            cur = cur.next
            old_cur.next = None
        pred_l.next = l_head.next
        return sentinel.next
                
            
           
            
       