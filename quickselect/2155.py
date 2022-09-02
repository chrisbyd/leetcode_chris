class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lpsum, rpsum = [0]* (n + 1),  [0] * (n+1)
        for i in range(n):
            lpsum[i+1] = lpsum[i] if nums[i] else 1 + lpsum[i]
        for i in range(n-1, -1, -1):
            rpsum[i] = rpsum[i+ 1] if not nums[i] else 1 + rpsum[i+1]
        print(lpsum, rpsum)
        res = []
        for i in range(n+ 1):
            res.append(lpsum[i] + rpsum[i])
        maxval = max(res)
        ans = []
        for idx , num in enumerate(res):
            if num == maxval:
                ans.append(idx)
        return ans
        