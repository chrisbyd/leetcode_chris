from typing import List
###bitmasking
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        def backtrack(index, sessions):
            if index == n:
                return True
            for i, session in enumerate(sessions):
                if session >= tasks[index]:
                    sessions[i] -= tasks[index]
                    if backtrack(index + 1, sessions):
                        return True
                    sessions[i] += tasks[index]
            return False
        l, r = 1, len(tasks)
        while l <= r:
            mid = (l + r) // 2
            sts = [sessionTime] * mid
            if backtrack(0, sts):
                r = mid - 1
            else:
                l = mid +1
        return l
                
        
        
        