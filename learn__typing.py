from typing import List, Type, TypeVar

T = TypeVar("T")


class Base:
    def __init__(self, a):
        self.a = a

    @classmethod
    def to_list(cls: Type[T], list_of_dict: list) -> List[T]:
        return [cls(**d) for d in list_of_dict]


class A(Base):
    @property
    def b(self):
        return self.a * 2


def test() -> List[A]:
    return A.to_list([{"a": 1}, {"a": 3}])


# Expected type 'List[A]', got 'List[Type[A]]' instead
