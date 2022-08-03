
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        def backtrack(index, res):
            if index  == n:
                ans.append(res)
            else:
                backtrack(index+ 1, res + [nums[index]])
                while index < n-1 and nums[index] == nums[index +1]:
                    index +=1 
                backtrack(index + 1,res)
        backtrack(0, [])
        return ans
    
               
