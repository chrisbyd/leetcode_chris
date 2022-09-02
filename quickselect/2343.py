from typing import List
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        n = len(nums)
        for k, t in queries:
            new_nums = [int(num[-t: ]) for num in nums]
            old_nums = new_nums.copy()
            new_nums.sort()
            ksmall = new_nums[k-1]
            count = 0
            for i in range(k):
                if new_nums[i] == ksmall:
                    count += 1
            print(count)
            for i in range(n):
                if old_nums[i] == ksmall:
                    if count == 1:
                        ans.append(i)
                        break
                    count -= 1
        return ans

## you  could solve it with priotiyy queu which is more clearn
nums = ["102","473","251","814"]
queries = [[1,1],[2,3],[4,2],[1,2]]
sol = Solution()
res = sol.smallestTrimmedNumbers(nums, queries)
print(res)