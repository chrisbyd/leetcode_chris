from typing import List

## detecting a cycle is wrong


    
# class Solution:
#     def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
#         left, right = set(), set()
#         for value in leftChild:
#             if value == -1:
#                 continue
#             if value in left:
#                 return False
#             else:
#                 left.add(value)
        
#         for value in rightChild:
#             if value == -1:
#                 continue
#             if value in right:
#                 return False
#             else:
#                 right.add(value)
        

#         if left & right:
#             return False
       

#         lmap, rmap = {}, {}
#         for i in range(n):
#             lmap[leftChild[i]] = i
#             rmap[rightChild[i]] = i
#         visited = set() 
#         memo = {}
#         def findRoot(node):
            
#             if node in memo:
#                 return memo[node]
#             if node in visited:
#                 return None
#             visited.add(node)
#             if node not in lmap and node not in rmap:
#                 memo[node] = node
#                 return node
#             else:
#                 if node in lmap:
#                     ans = findRoot(lmap[node])        
#                 else:
#                     ans = findRoot(rmap[node])
#                 memo[node] = ans
#                 return ans
            
#         roots = set()
#         for i in range(n):
#             root = findRoot(i)
#             if  root is None:
#                 return False
#             roots.add(root)
#             if len(roots) > 1:
#                 return False
#         return True

                
            
# sol = Solution()
# n = 2
# l = [1, 0]
# r = [-1,-1]
# n = 4
# l = [1,-1,3,-1]
# r = [2,-1,-1,-1]
# res = sol.validateBinaryTreeNodes(n, l, r)
# print(res)

from typing import List
from collections import deque
## detecting a cycle is wrong


    
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = -1
        children = set(leftChild)  | set(rightChild)
        for i in range(n):
            if i not in children:
                if root != -1:
                    return False
                else:
                    root = i
        if root == -1: return False
        q = deque([root])
        visited = set()
        count = 0
        while q:
            count += 1
            node = q.popleft()
            visited.add(node)
            for c in [leftChild[node], rightChild[node]]:
                if c == -1: continue
                if c in visited: return False
                visited.add(c)
                q.append(c)
        return count == n
                
        
sol = Solution()

n = 4
l = [1,0,3,-1]
r = [-1,-1,-1,-1]
res = sol.validateBinaryTreeNodes(n, l, r)
print(res)
