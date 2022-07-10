
from typing import List

class Btree:
    def __init__(self, value) -> None:
        self.value = value 
        self.left = None
        self.right = None
    
    def print_tree(self):
        ans = []
        def dfs(node):
            if node is None:
                return [None]
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                return [node.value, left, right]
        ans = dfs(self)
    
    
# test = Btree(0)
# test.left = Btree(2)
# test.right = Btree(3)
# test.left.right = Btree(3)
# ans = test.print_tree()
# print(ans)
    

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Btree(2)
        for num in nums:
            this_root = root
            for k in range(31,-1,-1):
                value = (num >> k) & 1
          
                thisNode = Btree(value)
                if value == 1 and this_root.right is None:
                    this_root.right = thisNode
                    this_root = this_root.right
                elif value == 0 and this_root.left is None:
                    this_root.left = thisNode
                    this_root = this_root.left
                elif value == 1 and this_root.right is not None:
                    this_root = this_root.right
                else:
                    this_root = this_root.left
         
            this_root.left = Btree(num)
        ans = 0
    
        for num in nums:
            thisnode = root
            for k in range(31,-1,-1):
                value = (num >> k) & 1
                #print(value)
                if value == 1 and thisnode.left is not None:
                    thisnode = thisnode.left
                elif value == 1 and thisnode.left is  None:
                    thisnode = thisnode.right
                elif value == 0 and thisnode.right is not None:
                    thisnode = thisnode.right
                else:
                    thisnode = thisnode.left
               # print(num, "this value:", value, "ndoe value", thisnode.value )
            curr_value = num ^ thisnode.left.value
           # print(num,thisnode.left.value, curr_value)
            if curr_value > ans:
                ans = curr_value
        return ans

# sol = Solution()
# nums = [3, 10 ,5]
# nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# nums = [3,10,5,25,2,8]
# res = sol.findMaximumXOR(nums)
# print(res)

 
                    


### another solution based on tries which i m familar with

class Node:
    def __init__(self) -> None:
        self.value = None
        self.next = [None, None]

class Solution1:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Node()
        for num in nums:
            cur_node = root
            for k in range(31, -1, -1):
                value = (num >> k) & 1
                if cur_node.next[value] is None:
                    cur_node.next[value] = Node()
                cur_node = cur_node.next[value]
            cur_node.value = num
        ans = 0
        for num in  nums:
            cur_node = root
            for k in range(31, -1, -1):
                value = (num >> k) & 1
                if cur_node.next[1 - value] is not None:
                    cur_node = cur_node.next[1 - value]
                else:
                    cur_node = cur_node.next[value]
            res = num ^ cur_node.value
            #print(num , cur_node.value, res)
            if res > ans:
                ans = res
                #print("the answer is",ans)
        return ans

sol = Solution1()
nums = [3, 10 ,5]
nums = [3,10,5,25,2,8]
res = sol.findMaximumXOR(nums)
print(res)

            
            




            
        


    
        
