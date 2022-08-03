# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         nums = []
#         for node_list in lists:
#             cur = node_list
#             while cur:
#                 nums.append(cur.val)
#                 cur = cur.next
#         nums.sort()
#         sentinel = ListNode()
#         cur = sentinel
#         for num in nums:
#             cur.next = ListNode(val = num)
#             cur = cur.next
#         return sentinel.next
        

from queue import PriorityQueue

from queue import PriorityQueue
###### be careful when using the priority queue, u need to make sure the priority value is unique
class PriorityEntry(object):

    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
    
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        index = 0
        for l in lists:
     
            if l:
                q.put(PriorityEntry(l.val, l))
        while not q.empty():
            entry = q.get()
            node = entry.data
            point.next = ListNode(node.val)
            point = point.next
            node = node.next
            if node:
                q.put(PriorityEntry(node.val, node))
        return head.next
        
        
a = ListNode(1, ListNode(4, ListNode(5)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = ListNode(2, ListNode(6))
lists = [a,b,b]
sol = Solution()
res = sol.mergeKLists(lists)
print(res)