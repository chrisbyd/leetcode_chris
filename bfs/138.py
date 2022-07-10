from typing import Optional
from collections import defaultdict

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        newNodeDict = {}
        curNode = head
        newNodeDict[curNode] = Node(curNode.val)
        while curNode.next:
            newNode = Node(curNode.next.val)
            newNodeDict[curNode.next] = newNode
            newNodeDict[curNode].next = newNode
            curNode = curNode.next
        curNode = head
        while curNode:
            randomNode = curNode.random
            newNodeDict[curNode].random = newNodeDict[randomNode] if randomNode else None
            curNode = curNode.next
        return newNodeDict[head]
            
            