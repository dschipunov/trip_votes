from util import SEPARATOR_LINE
from convert import ActionConverter, PersonConverter

class InputData:
    def __init__(self, name: str, action: int, vote: int):
        self.name = name
        self.action = action
        self.vote = vote

    def __str__(self):
        return f"InputData: '{self.name}', {self.action}, {self.vote}"

    @classmethod
    def from_input(cls):
        print(SEPARATOR_LINE)
        # Get inputs data
        name = input("Enter your name: ")
        action = input("Enter first number (1-15): ")
        person = input("Enter second number (1-15): ")

        cnv_action = ActionConverter()
        cnv_person = PersonConverter()

        return cls(name, cnv_action.convert(action), cnv_person.convert(person)) 