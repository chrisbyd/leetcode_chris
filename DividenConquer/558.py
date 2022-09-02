
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        def dfs(node1, node2):
            if node1.isLeaf and node2.isLeaf:
                return Node(node1.val or node2.val,  1 , None, None, None, None)
            elif node1.isLeaf and not node2.isLeaf:
                if node1.val == 1:
                    return node1
                else:
                    return node2
            elif not node1.isLeaf and node2.isLeaf:
                if node2.val == 1:
                    return node2
                else:
                    return node1
            else:
                tl = dfs(node1.topLeft, node2.topLeft)
                tr = dfs(node1.topRight, node2.topRight)
                bl = dfs(node1.bottomLeft, node2.bottomLeft)
                br =dfs(node1.bottomRight, node2.bottomRight)
                if sum([tl.isLeaf, tr.isLeaf, bl.isLeaf, br.isLeaf]) == 4:
                    sum_val = sum([tl.val, tr.val, bl.val, br.val])
                    if sum_val == 4 :
                        return Node(val = 1, isLeaf = 1)
                    if sum_val == 0:
                        return Node(val = 0, isLeaf = 1)
                return Node(val = 1, isLeaf = 0, topLeft = tl, topRight = tr, bottomLeft = bl, bottomRight = br)
        return dfs(quadTree1, quadTree2)
                
                    
                    
            
        