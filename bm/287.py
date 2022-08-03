## brutal force will result in tle
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            find = False
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    find = True
                    
            if  find: return nums[i]
            
                
###negative marking
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            cur = abs(nums[i])
            if nums[cur] < 0:
                ans = cur
            else:
                nums[cur] = -1 * nums[cur]
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return ans

## array a hashmap
###negative marking
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = 0
        while temp != nums[temp]:
            nums[temp], temp = temp, nums[temp]
        return temp
            
    
            
                
        