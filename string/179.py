from typing import List

# brutal force solution
# Not accepted with TLE 
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(num1, num2):
            for i in range(len(num1)):
                if int(num1[i]) > int(num2[i]):
                    return True
                elif int(num1[i]) < int(num2[i]):
                    return False
            return True
        self.ans = "".join(str(0) for i in range(len(nums)))
        if sum(nums) == 0:
            return "0"
        def dfs(nums, c_result):
            if not nums and compare(c_result, self.ans):
                self.ans = c_result
            elif  c_result and c_result[0] == '0':
                return 
            else:
                for idx, num in enumerate(nums):
                    nums.pop(idx)
                    dfs(nums, c_result + str(num))
                    nums.insert(idx, num)
        dfs(nums, "")
        return self.ans



# another solution
# The algorithm is dope

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        sorted_list = sorted(nums_str, key= LargerNumKey)
        return '0' if sum(nums) == 0 else ''.join(sorted_list)



sol = Solution()
nums = [1,2,3,4,5,6,7,8,9,0]
res= sol.largestNumber(nums)
print(res)
