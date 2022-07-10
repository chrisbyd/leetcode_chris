from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key= lambda x: x[0])
        print(people)
        ans = [[] for i in range(len(people))]
        for peo in people:
            count = peo[1]
            for i in range(len(people)):
                if count == 0 and len(ans[i]) == 0:
                    ans[i] = peo
                if len(ans[i]) == 0 or ans[i][0] >= peo[0]:
                    count -= 1
        return ans
 
sol = Solution()
people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
res = sol.reconstructQueue(people)
print(res)










        