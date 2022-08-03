from typing import List
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hour = [1,2,4,8]
        minute = [1, 2,4,8,16,32]
        ans_h = []
        ans_m = []
        def dfs(cur, inp, length, cur_res, ans,  maximum):
            if len(cur_res) == length:
                if not cur_res: cur_res.append(0)
                ans.append(cur_res)
                return
            elif cur == len(inp) or sum(cur_res) >= maximum:
                return
            else:
                dfs(cur+1, inp,length, cur_res + [inp[cur]], ans, maximum)
                dfs(cur + 1,inp, length, cur_res, ans, maximum)
        for i in range(4):
            n_ans_h = []
            n_ans_m = []
            dfs(0, hour, i, [],  n_ans_h, 11)
            dfs(0, minute, turnedOn - i, [], n_ans_m, 59)
            ans_h.append(n_ans_h)
            ans_m.append(n_ans_m)
        res = []
        for i in range(4):
            length = len(ans_h[i])
            length1 = len(ans_m[i])
            for j in range(length):
                for k in range(length1):
                    if ans_m[i]:
                        first = str(sum(ans_h[i][j]))
                        second = str(sum(ans_m[i][k])) if sum(ans_m[i][k]) >= 10 else "0" +  str(sum(ans_m[i][k]))
                        if int(first) > 11 or int(second) >59:
                            continue
                        res.append(first + ":" + second)
        return res
                    
sol = Solution()
target = 2
res = sol.readBinaryWatch(target)
print(res)
                
from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        LEDs = [1,2,4,8,1,2,4,8,16,32]
        ans = []
        def dfs(LEDs, index, hours, mins, n):
            if sum(hours) >= 12 or sum(mins) >= 60:
                return
            elif n == 0:
                h = str(sum(hours)) if hours else "0" 
                if not mins:
                    m = '00'
                else:
                    m =  str(sum(mins)) if sum(mins) >= 10 else "0" + str(sum(mins))
                ans.append(h + ':' + m)
                return
            elif index >= len(LEDs):
                return
            else:
                if index < 4:
                    dfs(LEDs, index + 1, hours + [LEDs[index]], mins, n-1)
                else:
                    dfs(LEDs, index +1 ,hours, mins + [LEDs[index]], n-1)
                dfs(LEDs, index +1, hours, mins, n)
        dfs(LEDs, 0, [], [], turnedOn)
        return ans

                
sol = Solution()
target = 2
res = sol.readBinaryWatch(target)
print(res)
                
####

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for h in range(12):
            bits_h = 0
            for i in range(4):
                if (h>>i) & 1 == 1:
                    bits_h +=1
            for m in range(60):
                cur_bits = bits_h
                for i in range(6):
                    if (m >> i) & 1:
                        cur_bits += 1
                if cur_bits == turnedOn:
                    mins = str(m) if m >= 10 else '0' + str(m)
                    ans.append(str(h) + ':' + mins)
        return ans

