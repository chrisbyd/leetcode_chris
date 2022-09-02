class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        set1 = set()
        set2= set()
        for c1, c2 in paths:
            set1.add(c1)
            set2.add(c2)
        res = set2 - (set1 & set2)
        return list(res)[0]
        