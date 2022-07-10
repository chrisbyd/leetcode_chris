from typing import List
from collections import Counter
from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_Freq = max(count.values())
        freq_dict = defaultdict(int)
        for val in count.values():
            freq_dict[val] += 1
        if n >= len(count.keys()):
            return (max_Freq - 1) * (n+1) + freq_dict[max_Freq]
        else:
            return max((max_Freq - 1) * (n+1) + freq_dict[max_Freq], len(tasks))
        
        
        
        
        