from typing import List
import random
class RandomizedCollection:

    def __init__(self):
        self.hashmap = {}
        self.values = []
        
    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = set([len(self.values)])
            self.values.append(val)
         
            return True
        else:
            self.hashmap[val].add(len(self.values))
            self.values.append(val)
          
            return False
        
    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        elif len(self.hashmap[val]) == 1:
            index = self.hashmap[val].pop()
            self.hashmap.pop(val)
        else:
            index = self.hashmap[val].pop()
        end_idx = len(self.values) - 1
        if index != end_idx:
            self.hashmap[self.values[-1]].remove(end_idx)
            self.hashmap[self.values[-1]].add(index)
            self.values[index], self.values[end_idx] = self.values[end_idx], self.values[index]
            self.values.pop()
        else:
            self.values.pop()
        
        return True

    def getRandom(self) -> int:
        
        ran = random.random()
        ran_dx = int( len(self.values) * ran )
     
        return self.values[ran_dx]




        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

randomizedSet = RandomizedCollection()
a = randomizedSet.insert(0)
print(a)

a = randomizedSet.insert(1)
print(a)
a = randomizedSet.remove(0) 
print(a)


a = randomizedSet.insert(2) 
print(a)
a = randomizedSet.remove(1)
print(a)
a = randomizedSet.getRandom() 
print(a)