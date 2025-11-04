from abc import ABC, abstractmethod

class AbstractConverter(ABC):
    @abstractmethod
    def convert(self, value: str)-> int:
        pass

class ActionConverter(AbstractConverter):
    def convert(self, value: str)-> int:
        ivalue = int(value)
        if 1 <= ivalue <= 7:
            return 1
        elif 8 <= ivalue <= 15:
            return 2
        else:
            raise ValueError(f"Action input value is out of range (1-15): {value}")
        

class PersonConverter(AbstractConverter):
    def convert(self, value: str)-> int:
        ivalue = int(value)

        return PersonConverter._convert(ivalue, 1, 15)

    @staticmethod
    def _convert(value: int, min: int, max: int) -> int:
        third = round(max / 3) 
        middle = third * 2

        if min <= value <= third:
            return 1
        elif (third + 1) <= value <= (middle):
            return 2
        elif (middle + 1) <= value <= max:
            return 3
        else:
            raise ValueError(f"Person input value is out of range (1-15): {value}")