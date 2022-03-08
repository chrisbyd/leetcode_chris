from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        res = [[nums[0]]]
        pos = 0
        prev = nums[0]
        for num in nums[1:]:
            if num - prev == 1:
                res[pos].append(num)
                prev = num
            else:
                res.append([])
                prev = num
                pos += 1
                res[pos].append(num)
        output = ['{}'.format(ls[0]) if len(ls) == 1 else '{}->{}'.format(ls[0],ls[-1])  for ls in res]
        return output

sol = Solution()
nums = []
res = sol.summaryRanges(nums)
print(res)
        



        