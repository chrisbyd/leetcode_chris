from typing import List

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1,len(num) +1):
            start = num[:i]
            if start[0] == '0' and len(start) != 1:
                continue
            else:
                start = int(start)
            for j in range(i+1, len(num) + 1): 
                index = j
                prev = start 
                res =  num[i:j]
                if res[0] == '0' and len(res) != 1:
                    continue
                else:
                    res = int(res)
                find = False
                while index < len(num):
                    find = True
                    interim = prev + res
                    prev = res
                    res = interim
                    if index + len(str(res)) <= len(num):
                        if str(res) == num[index: index+len(str(res))]:
                            index = index + len(str(res))
                        else:
                            find = False
                            break
                    else:
                        find = False
                        break
                if find:
                    return True
        return False


sol = Solution()


num = "101"
res = sol.isAdditiveNumber(num)
print(res)
