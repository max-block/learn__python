import base64
import pickle
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List


@dataclass
class Data:
    name: str
    value: Decimal
    tags: List[str]
    created_at: datetime


def t1():
    data = {
        "a": 1,
        "b": "bla",
        "c": Decimal("9.2343"),
        "d": True,
        "e": [1, 2, 3, 4],
        "f": datetime.now(),
        "g": Data("n1", Decimal("234.211"), ["a", "b"], datetime.now()),
    }
    res = pickle.dumps(data)
    pickled = base64.b64encode(res).decode("utf-8")

    print(pickled)

    decoded = pickle.loads(base64.b64decode(pickled))
    print(decoded)
    # {'a': 1, 'b': 'bla', 'c': Decimal('9.2343'), 'd': True, 'e': [1, 2, 3, 4], 'f': datetime.datetime(2020, 7, 15, 10, 13, 0, 829413), 'g': Data(name='n1', value=Decimal('234.211'), tags=['a', 'b'], created_at=datetime.datetime(2020, 7, 15, 10, 13, 0, 829424))} # noqa


if __name__ == "__main__":
    t1()
