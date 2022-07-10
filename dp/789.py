from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dis1 = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            dis = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if dis <= dis1:
                return False
        return True

        