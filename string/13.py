from  typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"M" :1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, 'L': 50, "XL": 40, "X": 10, 'IX': 9, "V": 5, "IV": 4, "I": 1}
        i= 0
        ans = 0
        while i < len(s) - 1:
            if s[i:i+2] in d.keys():
                ans += d[s[i:i+2]]
                i += 2
            else:
                ans += d[s[i]]
                i += 1
        if i == len(s) -1:
            ans += d[s[i]]
        return ans 

sol = Solution() 
s = "MMM"
res = sol.romanToInt(s)
print(res)



        