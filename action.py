import random
from enum import Enum

class Action(Enum):
    STAY = 1
    GO = 2

RND_ACTION_MIN = 1
RND_ACTION_MAX = 10
RND_ACTION_ITERATIONS = 5

class ActionValueRandomizer:
    def __init__(self, min: int = RND_ACTION_MIN, max: int = RND_ACTION_MAX, count: int = RND_ACTION_ITERATIONS):
        self.values = []
        for i in range(1, count+1):
            self.values.append(self.__action_value(min, max))
    
    def value(self) -> int:
        return round(sum(self.values) / len(self.values))
    
    def __action_value(self, min: int, max: int)-> int:
        sv = random.randint(min, max) 
        if min <= sv <= int(max / 2):
            return 1
        else:
            return 2   