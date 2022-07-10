from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dic = {}
        for num in nums:
            if num not in count_dic:
                count_dic[num] = 1
            else:
                count_dic[num] = count_dic[num] + 1 
        
        largest = 0
        res = 0
        for key in count_dic:
            if count_dic[key] > largest:
                res = key
                largest = count_dic[key]
        

        return res

sol = Solution() 
nums =  [2,2,1,1,1,2,2]
res = sol.majorityElement(nums)
print(res)