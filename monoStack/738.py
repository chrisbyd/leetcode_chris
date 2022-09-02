class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = list(str(n))
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                while i >= 1 and nums[i - 1] == nums[i]:
                    i -= 1
                nums[i] = str(int(nums[i]) - 1)
                ans = ''.join(nums[:i+1]) + '9'* (len(nums) - i - 1)
                return int(ans)
        return int(''.join(nums))

        

        
sol = Solution()
n = 1234
res = sol.monotoneIncreasingDigits(n)
print(res)

###monotone increasing with stack
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        nums = [int(x) for x in str(N)] # digits 
        stack = []
        for i, x in enumerate(nums): 
            while stack and stack[-1] > x: x = stack.pop() - 1
            stack.append(x) 
            if len(stack) <= i: break 
        return int("".join(map(str, stack)).ljust(len(nums), "9")) # right padding with "9"