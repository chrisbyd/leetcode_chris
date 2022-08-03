class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0

        for i in range(30, -1, -1):
            num = (1 << i)
            if num & left == num & right:
                digit = 1 if num & left >0 else 0
                ans += (digit << i)
            else:
                break

        return ans
