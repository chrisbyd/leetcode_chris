from typing import List


# time limit exceeds
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        dp = [set() for i in range(len(arr))]
        dp[0].add(arr[0])
        for i in range(1, len(arr)):
            for ele in dp[i-1]:
                dp[i].add(ele|arr[i])
            dp[i].add(arr[i])
        ans = set()
        for s in dp:
            ans = ans.union(s)
        return len(ans)

sol = Solution()
arr = [1,2,4]
arr = [13,4,2]
res = sol.subarrayBitwiseORs(arr)
print(res)


# I figre out the reason for the time limit is the union operation
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        dp = [set() for i in range(len(arr))]
        dp[0].add(arr[0])
        ans_set = set(arr)
        for i in range(1, len(arr)):
            for ele in dp[i-1]:
                dp[i].add(ele|arr[i])
                ans_set.add(ele|arr[i])
            dp[i].add(arr[i])
      
        return len(ans_set)
        

        