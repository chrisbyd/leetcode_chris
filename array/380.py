from typing import List
import random
class RandomizedSet:

    def __init__(self):
        self.original_set = set()
        

    def insert(self, val: int) -> bool:
        if val in self.original_set:
            return False
        self.original_set.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.original_set:
            return False
        self.original_set.remove(val)
        return True
        

    def getRandom(self) -> int:
        set_to_list = list(self.original_set)
        a = random.random()
        random_index = int( a * len(set_to_list))
        return set_to_list[random_index]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
randomizedSet = RandomizedSet()
a = randomizedSet.insert(1)
print(a)
a = randomizedSet.remove(2) 
print(a)
a = randomizedSet.insert(2)
print(a)
a = randomizedSet.getRandom()
print(a)
a = randomizedSet.remove(1)
print(a)
a = randomizedSet.insert(2) 
print(a)
a = randomizedSet.getRandom() 
print(a)
a = randomizedSet.insert(1)
a = randomizedSet.insert(3)
a = randomizedSet.insert(4)
a = randomizedSet.insert(5)
a = randomizedSet.getRandom() 
print(a)