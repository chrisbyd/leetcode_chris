from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        num2freq = Counter(s)
        total_num = len(num2freq)
        freq_list = sorted(list(num2freq.values()))[::-1]
        freq_index_dict = {}
        for index, freq in enumerate(freq_list):
            if freq not in freq_index_dict:
                freq_index_dict[freq] = index
        ans =["" for i in range(total_num)]
        for char in num2freq.keys():
            freq = num2freq[char]
            index = freq_index_dict[freq]
            while len(ans[index]) !=0:
                index += 1
            ans[index] = freq* char
        return "".join(ans)

from collections import Counter
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        char2freq = Counter(s)
        freq2char = defaultdict(list)
        for char in char2freq.keys():
            freq = char2freq[char]
            freq2char[freq].append(char)
        freq_list = sorted(list(freq2char.keys()))[:: -1]
        ans = ""
        for freq in freq_list:
            for char in freq2char[freq]:
                ans += freq * char
        return ans
        
        
        