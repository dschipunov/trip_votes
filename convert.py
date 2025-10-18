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
        if 1 <= ivalue <= 5:
            return 1
        elif 6 <= ivalue <= 10:
            return 2
        elif 11 <= ivalue <= 15:
            return 3
        else:
            raise ValueError(f"Person input value is out of range (1-15): {value}")