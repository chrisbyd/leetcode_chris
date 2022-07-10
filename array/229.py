from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        thres = int(len(nums)/3)
        nums.sort()
        count = 1
        res = []
        prev = nums[0]
        for num in nums[1:]:
            if num == prev:
                count += 1
            elif  count > thres:
                res.append(prev)
                count = 1
            else:
                count = 1
            prev = num
        if count > thres:
            res.append(prev)
        return res

sol = Solution() 
nums = [4,1,3,1,3,3,1,2,3,2,4,2,1,4,4,4,4,4]
out = sol.majorityElement(nums)
print(out)

class Solution1:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = {}
        output = []
        thres = int(len(nums) / 3)
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            elif hashMap[num] != -1:
                hashMap[num] += 1
            if hashMap[num] > thres :
                output.append(num)
                hashMap[num] = -1
        return output


sol = Solution1() 
nums = [2,2]
out = sol.majorityElement(nums)
print(out)  
        





        