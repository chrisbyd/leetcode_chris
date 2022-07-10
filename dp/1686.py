import re
from typing import List

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        def dp(player, avs, bvs):
            if len(avs) == 1:
                if player == 0:
                    return [avs[0], 0]
                else:
                    return [0, bvs[0]]
            else:
                if player == 0:
                    ans = [0, 0]
                    for i in range(len(avs)):
                        res = dp(1- player, avs[:i] + avs[i+1:], bvs[:i] + bvs[i+1:])
                        res[0] += avs[i]
                        ans = max(ans, res, key= lambda x: x[0])
                    return ans
                else:
                    ans = [0, 0]
                    for i in range(len(avs)):
                        res = dp(1- player, avs[:i] + avs[i+1:], bvs[:i] + bvs[i+1:])
                        res[1] += bvs[i]
                        ans = max(ans, res, key= lambda x: x[1])
                    return ans
        res = dp(0, aliceValues, bobValues)
        if res[0] > res[1]:
            ans = 1
        elif res[0] < res[1]:
            ans = -1
        else:
            ans = 0

        return ans

sol = Solution()
aliceValues = [2, 4, 3]
bobValues = [1, 6, 7]
res = sol.stoneGameVI(aliceValues, bobValues)
print(res)



class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        G = [ a + b for a, b in  zip(aliceValues, bobValues)]
        G.sort()
        n = len(aliceValues)
        biggest_alice = 0
        for i in range(n-1, -1, -2):
            biggest_alice += G[i]
        biggest_alice -= sum(bobValues)
        return 1 if biggest_alice > 0 else (-1 if biggest_alice <0 else 0)

        




sol = Solution()
aliceValues = [2, 4, 3]
bobValues = [1, 6, 7]
res = sol.stoneGameVI(aliceValues, bobValues)
print(res)