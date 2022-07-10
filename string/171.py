from typing import List

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        hmap = {1: 'A', 2: 'B', 3:'C', 4:'D', 5:"E", 6:'F', 7:'G', 8: 'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P',
        17:'Q', 18:'R', 19: "S", 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
        new_hmap = {}
        for key in hmap:
            new_hmap[hmap[key]] = key
        ans = 0
        for num in columnTitle:
            ans = ans * 26 + new_hmap[num]
        return ans

sol = Solution()
ct = "ZY"
res = sol.titleToNumber(ct)
print(res)


        