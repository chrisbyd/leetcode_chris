from typing import List
# Definition for a Node.
import copy
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        ans = copy.deepcopy(node)
        return ans
        
        
# Definition for a Node.
import copy
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        node_dict = {}
        def clone(node):
            if node.val in node_dict:
                return node_dict[node.val]
            else:
                nnode = Node(val = node.val)
                node_dict[node.val] = nnode
                nneighbors = []
                for neighbor in node.neighbors:
                    nneighbors.append(clone(neighbor))
                nnode.neighbors = nneighbors
                return nnode
        return clone(node)
    
                