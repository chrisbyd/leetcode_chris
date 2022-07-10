from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_dic = dict()
        for num in nums:
            if num not in freq_dic:
                freq_dic[num] = 1
            else:
                freq_dic[num] = freq_dic[num] + 1
        for key in freq_dic:
            if freq_dic[key] == 1:
                return key



class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        for i in range(1, length -1):
            if nums[i] != nums[i+1]:
                if nums[i] != nums[i-1]:
                    return nums[i]
        if len(nums) <=1 or nums[0] != nums[1]:
            return nums[0]
        return nums[-1]

        

nums = [0,1,0,1,0,1,99]
nums = [41]
sol = Solution1()
res = sol.singleNumber(nums)
print(res)