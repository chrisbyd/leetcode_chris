from typing import List


# backpacking problem
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def backtrack(index, current):
            if index < len(nums):
                if current and int(current.split()[-1]) > nums[index]:
                    backtrack(index+1, current)
                else:
                    backtrack(index+1, current + ' ' + str(nums[index]))
                    backtrack(index+1, current)
            else:
                if len(current.split()) >= 2:
                    ans.add(current)
        res = []
        backtrack(0, "")
        for string in ans:
            c_res = [int(char) for char in string.split()]
            res.append(c_res)
        return res





nums = [1,2,3,4,5,10]
sol = Solution()
res = sol.findSubsequences(nums)
print(res)

# another solution with dfs
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(nums, current):
            if len(current) >= 2 and current not in ans:
                ans.append(current[:])

            for i in range(len(nums)):
                if current and current[-1] > nums[i]:
                    continue
                current.append(nums[i])
                dfs(nums[i+1:], current)
                current.pop()
        dfs(nums, [])
        return ans


nums = [4,6,7,7]
sol = Solution()
res = sol.findSubsequences(nums)
print(res)


