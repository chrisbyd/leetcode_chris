from typing import List
import collections
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        cnt = collections.defaultdict(int)
        for x, y, a, b in rectangles:
            cnt[x,y] += 1
            cnt[x,b] -= 1
            cnt[a,b] += 1
            cnt[a,y] -= 1
        ans = 0
        for v in cnt.values():
            ans += abs(v)
        return True if ans == 4 else False



sol = Solution()
rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
res = sol.isRectangleCover(rectangles)
print(res)

class Solution1:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        dis_vertices = set()
        cnt = collections.defaultdict(int)
        count = 0
        cumu_area = 0
        res_area  = 0
        for x, y, a, b in rectangles:
            if cnt[x,y] == 0:
                dis_vertices.add((x,y))
                count += 1
            elif cnt[x,y] == 1:
                dis_vertices.remove((x,y))
                count -= 1
            if cnt[x,b] == 0:
                dis_vertices.add((x,b))
                count += 1
            elif cnt[x,b] == 1:
                dis_vertices.remove((x,b))
                count -= 1
            if cnt[a,b] == 0:
                dis_vertices.add((a,b))
                count += 1
            elif cnt[a,b] == 1:
                dis_vertices.remove((a,b))
                count -= 1
            if cnt[a,y] == 0:
                dis_vertices.add((a,y))
                count += 1
            elif cnt[a,y] == 1:
                dis_vertices.remove((a,y))
                count -= 1
            cnt[x,y] += 1
            cnt[x,b] += 1
            cnt[a,b] += 1
            cnt[a,y] += 1
            cumu_area += ((a - x) * (b- y))
        print(cumu_area)
        print(dis_vertices)
        if count == 4:
            width, length = 0, 0
            prev_x, pre_y = dis_vertices.pop()
            for x, y in dis_vertices:
                if x - prev_x != 0:
                    width = abs(x - prev_x)
                if y - pre_y != 0:
                    length = abs(y - pre_y)
            if cumu_area == width * length:
                return True
        
        return False
  


sol = Solution1()
rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
rectangles = [[0,0,1,1],[0,1,1,2],[0,2,1,3],[1,0,2,1],[1,0,2,1],[1,2,2,3],[2,0,3,1],[2,1,3,2],[2,2,3,3]]
res = sol.isRectangleCover(rectangles)
print(res)
 

        
