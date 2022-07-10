

#bit mask solution
#brutal force solution
# import math
# import re
# class Solution:
#     def maxProduct(self, s: str) -> int:
#         n = len(s)
#         ans = 0
#         hmap = {}
#         def isPalidrome(number):
#             res = ''
#             length = 0
#             for i in range(n):
#                 if 1 << i & number:
#                     res = s[n-1-i] + res
#                     length += 1
#             if res == res[::-1]:
#                 return length
#             return 0

#         for i in range(int(math.pow(2,n))):
#             if isPalidrome(i):
#                 hmap[i] = isPalidrome(i)
        
#         for k1 in hmap.keys():
#             for k2 in hmap.keys():
#                 if k1 & k2 == 0:
#                     ans = max(ans, hmap[k1] * hmap[k2])
#         return ans

# sol = Solution()
# s = "leetcodecom"
# res = sol.maxProduct(s)
# print(res)

# # recursion and backtracking solution
# # Tle 
# class Solution:
#     ans = 0
#     def maxProduct(self, s: str) -> int:
#         def isPalidrome(s):
#             if s == s[::-1]:
#                 return True
#             return False

#         def solve(index, s1, s2):
#             if index >= len(s):
#                 if isPalidrome(s1) and isPalidrome(s2):
#                     self.ans = max(self.ans, len(s1) * len(s2))
#             else:
#                 solve(index+1, s1 + s[index], s2)
#                 solve(index+1, s1, s2 + s[index] )
#                 solve(index+1, s1, s2)
#         solve(0, "", "")
#         return self.ans
            
            


# sol = Solution()
# s = "leetcodecom"
# res = sol.maxProduct(s)
# print(res)


class Solution:
    
    
    def maxProduct(self, s: str) -> int:
        res  = {}
        ans = 0
        def isPalidrome(s):
            if s == s[::-1]:
                return True
            return False
        
        def solve(index, s1, n1):
            if index >= len(s):
                if isPalidrome(s1):
                    res[n1] = len(s1) 
            else:
                solve(index+1, s1 + s[index], n1*2+1)
                solve(index+1, s1, n1*2)
        solve(0, "", 0)
        for n1 in res.keys():
            for n2 in res.keys():
                if not n1 & n2:
                    ans = max(ans, res[n1] * res[n2])
        return ans
            
            

sol = Solution()
#s = "leetcodecom"
s = 'bb'
res = sol.maxProduct(s)
print(res)
