from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPalidrome(input):
            if input == input[::-1]:
                return True
            return False

        def backtrack(s, c_list):
            if len(s) == 0:
                ans.append(c_list[:])
            else:
                for i in range(len(s)):
                    if isPalidrome(s[:i+1]):
                        c_list.append(s[:i+1])
                        backtrack(s[i+1:], c_list)
                        c_list.pop()
        backtrack(s, [])
        return ans

sol = Solution()
s = "aab"
res = sol.partition(s)
print(res)



        


        