import random
import json

from inputs import InputData
from person import Person
from convert import PersonConverter


class Results:
    def __init__(self, act_value: int):
        self.map = dict()
        self.act_value = act_value
    
    def add_person(self, data: InputData):
        idx = self.__new_index()
        self.map[idx] = Person(data.name, data.action, self.act_value)

    def __str__(self):
        return json.dumps(self.map, default=Person._serializer, indent=4)

    def __new_index(self) -> int:
        if len(self.map) < 2:
            return self.__next()
        else:
            keys = self.__keys()
            for i in Person.ALL_INDEXES:
                if i not in keys:
                    return i
            return 0

    def __keys(self) -> list[int]:
        return [key for key in self.map]
    
    def values(self) -> list[Person]:
        return [v for v in self.map.values()]

    def __next(self) -> int:
        keys = self.__keys()
        while True:
            idx = self.__person_value(1, 99)
            if not idx in keys:
                break
        return idx

    def __person_value(self, min: int, max: int)-> int:
        sv = random.randint(min, max)
        return PersonConverter._convert(sv, min, max)
    
