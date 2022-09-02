from typing import List
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        readsign = False
        readdigit = False
        ans = '0'
        for char in s:
            if not readdigit:
                if not readsign and char == " ":
                    continue
                if not readsign and char in ['-', '+']:
                    readsign = True
                    if char == '-':
                        sign = -1
                elif char.isdigit():
                    ans += char
                    readdigit = True
                else:
                    break
            else:
                if not char.isdigit():
                    break
                else:
                    readdigit = True
                    ans += char
        ans = sign * int(ans)
        if ans > 2 ** 31- 1:
            ans = 2 **31 -1
        elif ans < - 2**31:
            ans = - 2**31
        return ans
            
        