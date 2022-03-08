from typing import List
import sortedcontainers
import bisect

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        temp = sortedcontainers.SortedList(nums[:k+1])
        for i in range(len(temp) -1):
            if temp[i+1] - temp[i] <= t:
                return True
        i = 0
        for j in range(k+1, len(nums)):
       
            num = nums[j]
            temp.remove(nums[i])
            temp.add(nums[j])
            print("The j is",j,"The temp list is" , temp)
            index = bisect.bisect_left(temp,num)
            print(" the insert index is", index)
            if (index >=1 and num - temp[index-1] <= t) or (index < k and temp[index +1] - num <= t):
                return True
            i += 1
        
        return False

sol = Solution()


nums = [1,14,23,45,56,2,3]
k = 1
t = 10
# nums = [1,5,9,1,5,9]
# k = 2
# t = 3
res = sol.containsNearbyAlmostDuplicate(nums, k, t)
print(res)