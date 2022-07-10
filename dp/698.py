from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        if abs(len(odd) - len(even)) > 1:
            return False
        sign, i, j = 0, 0, 0
        ans = []
        while i != len(odd) or j != len(even):
            if sign == 0:
                ans.append(even[i])
                i += 1
            else:
                ans.append(odd[j])
                j += 1
            sign = 1 - sign
        return ans

sol = Solution()
nums = [4, 2, 5, 7]
res = sol.sortArrayByParityII(nums)
print(res)
                 
# time limite exceeded but it is correct
# partition to K equal 
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        side_length = sum(nums) // k
        nums.sort()
        memo = {}
        def dp(visited, sides_complete, current):
            if (visited, sides_complete, current) not in memo:
                if sides_complete ==  k-1 :
                    ans = True
                else:
                    ans = False
                    for i in range(len(nums)):
                        if not visited & 1<< (len(nums)-1 -i):
                            if current + nums[i] < side_length:
                                ans = ans or dp(visited^1<< (len(nums)-1 -i), sides_complete, current + nums[i])
                            elif current + nums[i] == side_length:
                                ans = ans or dp(visited^1<< (len(nums)-1 -i), sides_complete + 1, 0)
                memo[visited, sides_complete, current]  = ans
                return ans
            else:
                return memo[visited, sides_complete, current]
        return dp(0, 0, 0)

sol = Solution()
nums = [2,2,2,2,3,4,5]
k = 4
res = sol.canPartitionKSubsets(nums, k)
print(res)


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        n, dp = len(nums), [0] * k
        nums.sort(reverse= True)
        def dfs(i):
            if i == n:
                return len(set(dp)) == 1
            for j in range(k):
                dp[j] += nums[i]
                if dp[j] <= target and dfs(i+1):
                    return True
                dp[j] -= nums[i]
            return False
        return nums[0] <= target and dfs(0)

sol = Solution()
nums = [2,2,2,2,3,4,5]
k = 4
res = sol.canPartitionKSubsets(nums, k)
print(res)


                    

                  




        
        