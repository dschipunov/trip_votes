from action import Action

class Person:
    ALL_INDEXES = [1,2,3]

    @staticmethod
    def _serializer(obj):
        if isinstance(obj, Person) or isinstance(obj, Action):
            return obj.to_dict()
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    def __init__(self, name: str, action: int, act_value: int):
        self.name = name
        self.act_value = act_value
        self.action = self.to_action(action)

    def __str__(self):
        return f"Person: '{self.name}', {self.action}"
    
    def to_dict(self):
        return {"name": self.name, "action": self.action}
    
    def to_action(self, act_num: int) -> Action:
        if self.act_value == act_num:
            return Action.GO
        else:
            return Action.STAY 