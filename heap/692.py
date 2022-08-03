from collections import Counter
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word2Freq = Counter(words)
        
        freq2word = defaultdict(list)
        for word in word2Freq.keys():
            freq = word2Freq[word]
            freq2word[freq].append(word)
        freqlist = sorted(list(freq2word.keys()), reverse = True)
        ans = []
        cur = 0
        while k > 0:
            freq = freqlist[cur]
            words = sorted(freq2word[freq])
            for word in words:
                ans.append(word)
                k -= 1
                if k == 0: break
            cur += 1
        
        return ans
        
#### with priority queue

from collections import Counter
from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word2Freq = Counter(words)
        heap, ans = [], []

        for word in word2Freq.keys():
            freq = word2Freq[word]
            heappush(heap, (-freq, word))
            
        while k > 0:
            _, word = heappop(heap)
            ans.append(word)
            k  -= 1
        return ans
            
        
        