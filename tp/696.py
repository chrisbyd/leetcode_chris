###o(n^2)  TLE

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s_l = list(s)
        ans = 0
        for i in range(len(s_l)):
            if s_l[i] == '0':
                n_zeros, n_ones = 1, 0
            else:
                n_ones, n_zeros =1, 0
            count = 0
            for j in range(i+ 1, len(s_l)):
                if s_l[j] != s_l[j-1]:
                    count += 1
                if count == 2:
                    break
                if s_l[j] == '0':
                    n_zeros += 1
                else:
                    n_ones += 1
              
                if n_zeros == n_ones:
                    ans += 1
        return ans
                
sol = Solution()
s = "00110011"
res = sol.countBinarySubstrings(s)
print(res)

###linear scan with groups
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                groups.append(1)
            else:
                groups[-1] += 1
        ans = 0
        for i in range(len(groups) - 1):
            ans += min(groups[i], groups[i+1])
        return ans
        
            
        
