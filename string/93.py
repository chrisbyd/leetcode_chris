from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtrack(s, res_list):
            if len(res_list) == 4 and len(s) == 0:
                ans.append('.'.join(res_list))
            elif len(res_list) != 4 and  len(s) !=0 :
                    if int(s[0]) >= 0:
                        res_list.append(s[0])
                        backtrack(s[1:], res_list)
                        res_list.pop()
                    if len(s) >= 2 and s[0] != '0':
                        res_list.append(s[0:2])
                        backtrack(s[2:], res_list)
                        res_list.pop()
                    if len(s) >= 3 and s[0] != '0' and int(s[0:3]) < 256 : 
                        res_list.append(s[0:3])
                        backtrack(s[3:], res_list)
                        res_list.pop()
        backtrack(s, [])
        return ans

sol = Solution()
s = "19216811"   
res = sol.restoreIpAddresses(s)
print(res)


        