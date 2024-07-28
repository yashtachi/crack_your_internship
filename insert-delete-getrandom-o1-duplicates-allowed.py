from collections import defaultdict
import random
class RandomizedCollection:

    def __init__(self):
        self.list = []
        self.dict =  defaultdict(set)
        

    def insert(self, val: int) -> bool:
        self.list.append(val)
        self.dict[val].add(len(self.list) - 1)

        return len(self.dict[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.dict[val]: 
            return False
        idx = self.dict[val].pop()
        last_num = self.list[-1]
        self.list[idx] = last_num
        self.dict[last_num].add(idx)
        self.dict[last_num].discard(len(self.list) - 1)
        self.list.pop()

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.list)