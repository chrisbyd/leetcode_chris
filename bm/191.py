class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = list(bin(n))[2:]
        ans = [int(v) for v in ans]
        return sum(ans)