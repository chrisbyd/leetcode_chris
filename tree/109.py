# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        return self.constructTree(head)
        
    def constructTree(self, head):
        value_list = []
        cur = head
        while cur:
            value_list.append(cur.val)
            cur = cur.next
        length = len(value_list)
        
        def dfs(v_list):
            if len(v_list) == 1:
                return TreeNode(val = v_list[0])
            elif len(v_list) == 0:
                return None
            else:
                length = len(v_list)
                mid = length // 2
                node = TreeNode(val = v_list[mid])
                node.left = dfs(v_list[:mid])
                node.right = dfs(v_list[mid+1:])
                return node
        return dfs(value_list)
                
    