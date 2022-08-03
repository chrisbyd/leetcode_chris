from typing import List

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         def dfs(nums,  cur):
#             if not nums:
#                 ans.append(cur)
#             else:
#                 dfs(nums[1:], cur + [nums[0]])
#                 dfs(nums[1:], cur )
#         dfs(nums, [])
#         return ans
        


#with bitmasking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            print(bitmask)
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output

sol = Solution()
nums = [1,2,3]
res = sol.subsets(nums)
print(res)


### with bitmasking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        n_th_bit  = 1 << n
        for i in range(2 ** n):
            bitmask = bin(i | n_th_bit)[3:]
            ans.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return ans
        
        