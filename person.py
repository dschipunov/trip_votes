from action import Action

class Person:
    def __init__(self, name: str, action: int, act_value: int):
        self.name = name
        self.act_value = act_value
        self.action = self.to_action(action)

    def __str__(self):
        return f"Person: '{self.name}', {self.action}"
    
    def to_action(self, act_num: int) -> Action:
        if self.act_value == act_num:
            return Action.GO
        else:
            return Action.STAY 