from enum import Enum


class Status(Enum):
    OK = "OK"
    DOWN = "DOWN"


values = [s.value for s in Status]
print(values)  # ['OK', 'DOWN']


print([s for s in Status])
