# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1, nums2 = [], []
        while l1:
            nums1.append(l1.val)
            l1 = l1.next
        while l2:
            nums2.append(l2.val)
            l2 = l2.next
        nums1, nums2 = nums1[::-1], nums2[::-1]
        n1, n2 = len(nums1), len(nums2)
        ans, l, r = [], 0, 0
        carry = 0
        while l < n1 and r < n2:
            val = nums1[l] + nums2[r] + carry
            carry = val // 10
            val = val % 10
            ans.append(val)
            l, r = l +1, r + 1
        while l < n1:
            val = nums1[l] + carry
            carry = val // 10
            val = val % 10
            ans.append(val)
            l += 1
        while r < n2:
            val = nums2[r] + carry
            carry = val // 10
            val = val % 10
            ans.append(val)
            r += 1
        if carry:
            ans.append(carry)
        sentinel = ListNode()
        cur = sentinel
        for num in reversed(ans):
            nnode = ListNode(val = num)
            cur.next = nnode
            cur = cur.next
        return sentinel.next




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1, nums2 = [], []
        while l1:
            nums1.append(l1.val)
            l1 = l1.next
        while l2:
            nums2.append(l2.val)
            l2 = l2.next
        nums1, nums2 = nums1[::-1], nums2[::-1]
        n1, n2 = len(nums1), len(nums2)
        if n2 >  n1: nums1 = nums1 + [0] * (n2 - n1)
        if n1 > n2: nums2 = nums2 + [0] * (n1 - n2)
        
        carry, prev = 0, None
        for lval, rval in zip(nums1, nums2):
            val = lval + rval + carry
            carry = val // 10
            val %= 10
            nnode = ListNode(val = val)
            nnode.next = prev
            prev = nnode
        if carry:
            nnode = ListNode(val = 1)
            nnode.next = prev
        return nnode
        