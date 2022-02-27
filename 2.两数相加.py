#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
       node = self.helper(l1,l2, 0)
       return node
        

    def helper(self,l1, l2, addition ):
        if l1 is None and addition == 0:
            return l2
        if l2 is None and addition == 0:
           return l1 
        if l1 is None and l2 is not None:
            new_val = (l2.val + addition)%10
            addition = (l2.val + addition)//10
            newNode = ListNode()
            newNode.val = new_val
            newNode.next = self.helper(None, l2.next, addition)
            return newNode
        if l1 is not None and l2 is None:
            new_val = (l1.val + addition)%10
            addition = (l1.val + addition)//10
            newNode = ListNode()
            newNode.val = new_val
            newNode.next = self.helper(l1.next,None, addition)
            return newNode
        
        if l2 is None and l1 is None:
            newNode = ListNode(1,None)
            return newNode
  
        newNode = ListNode()
        new_val = (l1.val+ l2.val + addition)%10
        addition = (l1.val+ l2.val + addition)//10
        newNode.val = new_val
        newNode.next = self.helper(l1.next,l2.next,addition)
        return newNode 

l1 = ListNode(9,ListNode(9,ListNode(9,None)))
l2 = ListNode(9,ListNode(9, None)  )      
sol = Solution()
res = sol.addTwoNumbers(l1,l2)
print(res.next.val)
# @lc code=end

