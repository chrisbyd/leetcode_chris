from typing import List
from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        q = deque([0])
        count = 0
        while q:
     
            room = q.pop()
            visited.add(room)
            count += 1
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)
        return count == len(rooms)

sol = Solution()
rooms = [[1,2],[2,1],[1]]
res = sol.canVisitAllRooms(rooms)
print(res)