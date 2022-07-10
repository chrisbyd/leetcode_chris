from tkinter.messagebox import NO
from typing import List
from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        q = deque([node])
        visited = {}
        constructed = {}
        new_root = Node(val = node.val)
        constructed[new_root.val] = new_root
        while q:
            cur_node = q.popleft()
          
            new_node = constructed[cur_node.val]
            if cur_node.val in visited:
                continue
            visited[cur_node.val] = True
            for n_node in cur_node.neighbors:
                if n_node.val not in constructed:
                    copy_node = Node(val = n_node.val)
                    constructed[n_node.val] = copy_node
                else:
                    copy_node = constructed[n_node.val]
                new_node.neighbors.append(copy_node)
                
                if n_node.val not in visited:
                    q.append(n_node)
        return new_root
                


#### recursive DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}
        
        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
                
            return copy
        
        return clone(node) if node else None


###### BFS
from collections import deque
class Solution:
    def cloneGraph(self, node : "Node") -> 'Node':
        if not node: return node
        curNewDict = {}
        q = deque([node])
        while q:
            curNode = q.popleft()
            if curNode not in curNewDict: curNewDict[curNode] = Node(val= curNode.val)
            for nNode in curNode.neighbors:
                if nNode not in curNewDict:
                    curNewDict[nNode] = Node(val= nNode.val)
                    q.append(nNode)
                curNewDict[curNode].neighbors.append(curNewDict[nNode])
        return curNewDict[node]



