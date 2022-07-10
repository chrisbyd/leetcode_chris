

def guess(num):
    pass
class Solution:
    def guessNumber(self, n: int) -> int:
        i, j = 1, n
        while i <= j:
            mid = (i + j) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                i = mid+1
            else:
                j = mid - 1
        return False

sol = Solution()
n = 10
pick = 6   
res = sol.guessNumber(n, pick)
print(res)