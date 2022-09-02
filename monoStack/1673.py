class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        ans = []
        remove = len(nums) - k
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and remove > 0:
                stack.pop()
                remove -= 1
            stack.append(num)
        ans = stack[: k]
        return ans
            
        