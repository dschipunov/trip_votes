import random

from inputs import InputData
from person import Person


class Results:
    all_indexes = [1,2,3]

    def __init__(self, act_value: int):
        self.cache = dict()
        self.act_value = act_value
    
    def add_person(self, data: InputData):
        idx = self.__get_index()
        self.cache[idx] = Person(data.name, data.action, self.act_value)

    def __str__(self):
        return f"act_value: {self.act_value}"


    def __get_index(self) -> int:
        if len(self.cache) < 2:
            return self.__next()
        else:
            keys = self.__keys()
            for i in Results.all_indexes:
                if i not in keys:
                    return i
            return 0
        
    def __keys(self) -> list[int]:
        return [key for key in self.cache]
    
    def values(self) -> list[Person]:
        return [v for v in self.cache.values()]

    def __next(self) -> int:
        keys = self.__keys()
        while True:
            idx = self.__person_value(1, 99)
            if not idx in keys:
                break
        return idx

    def __person_value(self, min: int, max: int)-> int:
        _third = round(max / 3)
        sv = random.randint(min, max) 
        if 1 <= sv <= _third:
            return 1
        elif (_third + 1) <= sv <= (_third * 2):
            return 2
        else:
            return 3 
