from tkinter import S
from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ''
        if numRows == 1:
            return s
        for i in range(numRows):
            j = i
            while j < len(s):
                if i == 0 or i == numRows -1:
                    ans = ans + s[j]
                else:
                    index = j + (numRows - i -1) * 2
                    if index < len(s):
                        ans = ans + s[j] + s[index]
                    else:
                        ans = ans + s[j] 
                j = j + (numRows -1) *2
        return ans 

sol = Solution()
s = "A"
numRows = 1
res = sol.convert(s, numRows)
print(res)
        