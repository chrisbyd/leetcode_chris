from typing import List


### it is accepted but it is too complicated
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstlen: int, secondlen: int) -> int:
        n = len(nums)
        dpltr_f = [0 for i in range(n- firstlen + 1)]
        dpltr_s = [0 for i in range(n - secondlen + 1)]
        dprtl_f = [0 for i in range(n - firstlen + 1 )]
        dprtl_s = [0 for i in range(n - secondlen + 1)]
        cum_sum = [0 for i in range(n)]
        ans = 0
        for i in range(n):
            ans += nums[i]
            cum_sum[i] = ans
        dpltr_f[0] = sum(nums[: firstlen])
        dpltr_s[0] = sum(nums[: secondlen])
        dprtl_f[-1] = sum(nums[n-firstlen:])
        dprtl_s[-1] = sum(nums[n-secondlen:])
        
        index = 1
        for i in range(firstlen, n):
            dpltr_f[index] = max(dpltr_f[index-1], cum_sum[i] - cum_sum[i - firstlen])
            index += 1
        index = 1
        for i in range(secondlen, n):
            dpltr_s[index] = max(dpltr_s[index-1], cum_sum[i] - cum_sum[i - secondlen])
            index += 1

        index = len(dprtl_f) - 2

        for i in range(n-firstlen-1, -1, -1):
            if i != 0:
                dprtl_f[index] = max(dprtl_f[index+1], cum_sum[i+firstlen-1] - cum_sum[i-1])
            else:
                dprtl_f[index] = max(dprtl_f[index+1], cum_sum[i+firstlen-1] - 0)
            index -= 1

        index = len(dprtl_s) - 2
        for i in range(n-secondlen-1, -1, -1):
            if i != 0:
                dprtl_s[index] = max(dprtl_s[index+1], cum_sum[i+secondlen-1] - cum_sum[i-1])
            else:
                dprtl_s[index] = max(dprtl_s[index+1], cum_sum[i+secondlen-1] - 0)
            index -= 1
        ans = -float('inf')

        for i in range(len(dpltr_f) - secondlen):
            ans = max(ans, dpltr_f[i] + dprtl_s[firstlen + i])
        for i in range(len(dpltr_s) - firstlen):
            ans = max(ans, dpltr_s[i] + dprtl_f[secondlen + i])
        return ans

            




sol = Solution()
nums = [0,6,5,2,2,5,1,9,4]
firstLen = 1
secondLen = 2

nums = [3,8,1,3,2,1,8,9,0]
firstLen = 3
secondLen = 2


nums = [2,1,5,6,0,9,5,0,3,8]
firstLen = 4
secondLen = 3
res = sol.maxSumTwoNoOverlap(nums, firstLen, secondLen)
print(res)

### a more easy dp solution

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstlen: int, secondlen: int) -> int:
        pass




####  sliding window
### it is reasonable since nums[i] > 0

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstlen: int, secondlen: int) -> int:
        def getMaxSubarraySum(arr, size):
            if len(arr) < size:
                return 0
            ans = sum(arr[:size])
            for i in range(1, len(arr) - size + 1):
                tem = ans - arr[i-1] + arr[i+ size - 1]
                ans = max(ans, tem)
            return ans
            
        n = len(nums)
        cumm = sum(nums[:firstlen])
        ans = cumm + getMaxSubarraySum(nums[firstlen:], secondlen)
        for i in range(1, n - firstlen +1):
            secondSum = max(getMaxSubarraySum(nums[:i], secondlen), getMaxSubarraySum(nums[i+firstlen:], secondlen))
            cumm = cumm - nums[i-1] + nums[i+firstlen - 1]
            ans = max(ans, cumm + secondSum)
        return ans



nums = [2,1,5,6,0,9,5,0,3,8]
firstLen = 4
secondLen = 3
nums = [0,6,5,2,2,5,1,9,4]
firstLen = 1
secondLen =2
res = sol.maxSumTwoNoOverlap(nums, firstLen, secondLen)
print(res)




            

        


