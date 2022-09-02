class Solution:
    def largestInteger(self, num: int) -> int:
        nums = [int(num) for num in list(str(num))]
        odds, odds_idx = [], []
        evens, evens_idx = [], []
        n = len(nums)
        for i, num in enumerate(nums):
            if num % 2 == 0:
                evens.append(num)
                evens_idx.append(i)
            else:
                odds.append(num)
                odds_idx.append(i)
        evens = sorted(evens, reverse = True)
        odds = sorted(odds, reverse = True)
        ans = [0] * n
        cur = 0
        for od in odds_idx:
            ans[od] = odds[cur]
            cur += 1
        cur = 0
        for ed in evens_idx:
            ans[ed] = evens[cur]
            cur += 1
        res = 0
        for num in ans:
            res = res * 10 + num
        return res
        